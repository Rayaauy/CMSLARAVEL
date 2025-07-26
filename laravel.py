import requests
from concurrent.futures import ThreadPoolExecutor
import os

def content_indicates_laravel(text):
    indicators = [
        "csrf_token()",
        "laravel",
        "app()->",
        "Whoops, looks like something went wrong"
    ]
    return any(ind.lower() in text.lower() for ind in indicators)

def headers_indicate_laravel(headers):
    powered_by = headers.get("x-powered-by", "").lower()
    cookie = headers.get("set-cookie", "").lower()
    return "laravel" in powered_by or "laravel_session" in cookie

def is_live(domain):
    try:
        r = requests.get(domain, headers={"User-Agent": "Mozilla/5.0"}, timeout=8)
        return r.status_code == 200
    except:
        return False

def is_laravel(domain):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.get(domain, headers=headers, timeout=10)
        if r.status_code != 200:
            return False
        if headers_indicate_laravel(r.headers) or content_indicates_laravel(r.text):
            return True

        env = requests.get(domain + "/.env", headers=headers, timeout=8)
        if "APP_KEY=" in env.text:
            return True

        server = requests.get(domain + "/server.php", headers=headers, timeout=8)
        if "laravel" in server.text.lower():
            return True

    except:
        pass
    return False

def scan_domain(domain):
    domain = domain.strip()
    if not domain.startswith("http"):
        domain = "http://" + domain

    if not is_live(domain):
        print(f"[!] Dead/Non-200: {domain}")
        return (domain, None)

    if is_laravel(domain):
        print(f"[+] Laravel Detected: {domain}")
        return (domain, True)
    else:
        print(f"[-] Not Laravel: {domain}")
        return (domain, False)

def main():
    print("=== Laravel Detection Tool (Interactive) ===")

    # Input dari user
    input_file = input("Masukkan nama file domain (.txt): ").strip()
    while not os.path.exists(input_file):
        print("File tidak ditemukan. Coba lagi.")
        input_file = input("Masukkan nama file domain (.txt): ").strip()

    output_laravel = input("Nama file output Laravel: ").strip()
    output_nonlaravel = input("Nama file output Non-Laravel: ").strip()

    try:
        threads = int(input("Jumlah thread (misal: 30): ").strip())
    except:
        threads = 20
        print("Input tidak valid. Default thread: 20")

    with open(input_file, 'r') as f:
        domains = list(set(f.read().splitlines()))  # hapus duplikat

    detected, not_detected = [], []

    print("\n🔎 Mulai scan...\n")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(scan_domain, domains)

    for domain, status in results:
        if status is True:
            detected.append(domain)
        elif status is False:
            not_detected.append(domain)

    # Simpan hasil
    with open(output_laravel, 'w') as f:
        f.write("\n".join(detected))
    with open(output_nonlaravel, 'w') as f:
        f.write("\n".join(not_detected))

    print("\n=== Scan Selesai ===")
    print(f"✔️ Laravel Detected: {len(detected)}")
    print(f"❌ Not Laravel: {len(not_detected)}")
    print(f"⛔ Dilewati (Non-200): {len(domains) - len(detected) - len(not_detected)}")
    print(f"\n📁 Output tersimpan di: {output_laravel}, {output_nonlaravel}")

if __name__ == "__main__":
    main()
