# 🔍 Smart Multi-Keyword Filter

Script Python sederhana namun powerful untuk memfilter baris-baris dari file berdasarkan **multi-kata kunci** seperti domain, path sensitif (`/login`, `/admin`), atau kata tertentu.

---

## 📌 Fitur

- 🎯 Filter menggunakan **lebih dari satu keyword** (dipisah koma).
- 🧠 Case-insensitive (tidak peduli huruf besar/kecil).
- 📁 Simpan hasil otomatis ke `filtered.txt`.
- ⚡ Lebih fleksibel dan cepat daripada `grep` biasa.

---

## 🚀 Cara Pakai

### 1. Persiapkan file list (contoh: `list.txt`)
Isi file kamu dengan format seperti ini:
example.com:root:toor123
webmail.go.id:admin:admin123
admin.site.net:super:superpass
login.example.go.id:root:bankpass


### 2. Jalankan script

```bash
git clone https://github.com/00x0kafyy/ULP-filter.git
cd ULP-filter
python smart_filter.py
```

### 3. Masukkan Nama File Dan Keyword Yang Ingin Di Filter
📄 Enter input filename (e.g. list.txt): list.txt
🔑 Enter keyword(s) to filter (e.g. go.id,/login,/admin): go.id,/login,/admin,webmail

### ✅ Output
```filtered.txt```
