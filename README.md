# 🕵️‍♂️ Laravel Detector - SPHINX101 Edition

**"If you're still poor, what do you have to fear?"** – Motivasi kecil biar tetap semangat nge-scan website. 😎

---

## ⚡ Apa Ini?

Tool Python untuk:
- Mengecek apakah sebuah domain menggunakan **Laravel** atau tidak.
- Memfilter hanya domain **live (HTTP 200)**.
- Bisa **multithreading** biar nggak nunggu sampai ubanan.
- Output otomatis ke file **laravel.txt** & **nonlaravel.txt**.
- Ada **banner ASCII kece** biar keliatan *pro hacker vibes™*.

---

## 🛠 Cara Pakai

1. Clone dulu repository ini:
   ```bash
   git clone https://github.com/username/laravel-detector.git
   cd laravel-detector

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan:

   ```bash
   python laravel_checker.py
   ```

   (Versi ini **interaktif**: kamu akan diminta masukkan file input, output, dan jumlah thread.)

---

## 📂 Format File Input

Buat file `list.txt`:

```
http://example.com
https://laravel-app.com
targetsite.org
```

---

## 🎯 Fitur Keren

✅ ASCII Banner supaya terasa kayak di film hacker.
✅ Bisa **atur jumlah threads** → scan makin cepat.
✅ Hanya scan **domain yang statusnya 200 OK**.
✅ Deteksi via header, cookie, konten HTML, `.env`, sampai `server.php`.
✅ Output rapi → `laravel.txt` & `nonlaravel.txt`.

---

## ⚠️ Catatan Penting

* Gunakan untuk **edukasi & security testing** pada domain **yang kamu miliki**.
* Jangan dipakai untuk iseng ke website orang lain → bisa masalah hukum.

---

## 👾 Preview Banner

```
     ____  ____  _   _ ___ _   ___  ___  ___  _ 
    / ___||  _ \| | | |_ _| \ | \ \/ / |/ _ \/ |
    \___ \| |_) | |_| || ||  \| |\  /| | | | | |
     ___) |  __/|  _  || || |\  |/  \| | |_| | |
    |____/|_|   |_| |_|___|_| \_/_/\_\_|\___/|_|

SPHINX101.GOV.ID
IF YOU'RE STILL POOR WHAT DO YOU HAVE TO FEAR?
============================================================
```

---

## 🖖 Support & Kontribusi

* Pull request welcome!
* Atau bikin **issue** kalau kamu nemu bug.
* Kalau suka → kasih ⭐ di repo ini (biar kami makin semangat ngoding).

---

## 📜 Lisensi

MIT License – bebas dipakai, jangan disalahgunakan.

---

> **"In hacking we trust, in Laravel we detect."** 😄

