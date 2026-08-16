# Panduan Upload GitHub & Deployment ke Streamlit Community Cloud

Aplikasi ini telah dirancang secara modular agar dapat dideploy langsung ke **Streamlit Cloud** secara gratis dan terhubung dengan repositori **GitHub** Anda.

**Author:** Abdurrahman Assegaf  
**Track:** ARC Prize 2026 - ARC-AGI-2 (Static Grid Reasoning)  

---

## 🚀 Bagian 1: Inisialisasi & Upload ke GitHub

### Langkah 1: Buka Terminal di Folder Proyek
Pastikan direktori terminal berada di `d:\ARC Prize 2026 - Paper Track`:

```bash
cd "d:\ARC Prize 2026 - Paper Track"
```

### Langkah 2: Inisialisasi Git dan Commit Semua File
Jalankan perintah berikut:

```bash
git init
git add .
git commit -m "feat: Initial commit ARC Prize 2026 Dual-System Solver & Streamlit Dashboard"
```

### Langkah 3: Buat Repository Baru di GitHub
1. Buka browser dan login ke [GitHub](https://github.com).
2. Klik tombol **New Repository** (atau tanda `+` di kanan atas -> *New repository*).
3. Beri nama repositori, contoh: `arc-prize-2026-paper-track` atau `arc-agi-dual-solver`.
4. Pilih **Public** (agar bisa dideploy langsung ke Streamlit Cloud gratis).
5. **Jangan centang** opsi *Add a README file* atau *.gitignore* (karena sudah ada di lokal).
6. Klik **Create repository**.

### Langkah 4: Hubungkan & Push ke GitHub
Salin URL repositori Anda dan jalankan:

```bash
# Ubah branch utama menjadi main
git branch -M main

# Tambahkan remote origin (Ganti URL dengan repo GitHub Anda)
git remote add origin https://github.com/USERNAME_GITHUB_ANDA/arc-prize-2026-paper-track.git

# Push seluruh kode ke GitHub
git push -u origin main
```

---

## ☁️ Bagian 2: Deployment ke Streamlit Community Cloud

Setelah kode berada di GitHub, Anda dapat meng-online-kan web app ini secara gratis:

1. Buka [https://share.streamlit.io](https://share.streamlit.io) atau [https://streamlit.io/cloud](https://streamlit.io/cloud).
2. Login menggunakan akun **GitHub** Anda.
3. Klik tombol **"Create app"** atau **"New app"**.
4. Isi formulir konfigurasi aplikasi:
   - **Repository:** Pilih repo GitHub Anda (misal `USERNAME/arc-prize-2026-paper-track`).
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`
   - **App URL (Opsional):** Anda bisa memilih nama custom URL (misal: `arc-prize-2026-abdurrahman`).
5. Klik **"Deploy!"**.
6. Streamlit Cloud akan menginstal dependensi dari `requirements.txt` dan aplikasi Anda akan live dalam waktu ~1 menit!

---

## 💻 Bagian 3: Menjalankan di Lokal (Opsional)

Jika ingin menjalankan aplikasi Streamlit di komputer lokal terlebih dahulu:

```bash
# 1. Pastikan dependensi terinstall
pip install -r requirements.txt

# 2. Jalankan server Streamlit lokal
streamlit run streamlit_app.py
```

Aplikasi akan otomatis terbuka di browser pada alamat `http://localhost:8501`.
