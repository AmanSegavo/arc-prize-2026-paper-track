# Panduan Lengkap Submission Kaggle: ARC Prize 2026 - Paper Track

**Author:** Abdurrahman Assegaf  
**Repository GitHub:** [https://github.com/AmanSegavo/arc-prize-2026-paper-track](https://github.com/AmanSegavo/arc-prize-2026-paper-track)  
**Track:** ARC-AGI-2 (Static Grid Reasoning)  

---

## 📋 Ikhtisar Persyaratan Kaggle Paper Track

Untuk memenuhi syarat penilaian dewan juri (François Chollet & Mike Knoop):
1. **Paper Write-up:** Ditulis langsung di platform write-up Kaggle dengan batas **maksimal 1.500 kata**.
2. **Cover Image Wajib:** Diunggah pada bagian *Media Gallery*.
3. **Public Notebook Wajib:** Ditautkan pada field *Project Links* (status notebook harus **Public**).
4. **Linked Submission:** Paper harus ditautkan ke submission kode aktif di kompetisi **ARC-AGI-2**.

---

## 🛠️ Langkah 1: Buat & Publikasikan Kaggle Notebook

1. Buka [Kaggle](https://www.kaggle.com/) dan login.
2. Di pojok kiri atas, klik **Create (+) $\to$ New Notebook**.
3. Beri judul notebook:  
   `ARC Prize 2026: Dual-System Neuro-Symbolic Solver`
4. Di panel sebelah kanan (*Data Explorer*), klik **Add Input** $\to$ cari dan tambahkan dataset **ARC Prize** (atau `arc-prize-2024` / `arc-prize-2026`).
5. Di sel pertama notebook, Anda bisa langsung mengklon kode repositori GitHub Anda:
   ```python
   # Clone codebase lengkap dari GitHub
   !git clone https://github.com/AmanSegavo/arc-prize-2026-paper-track.git
   import sys
   sys.path.append("arc-prize-2026-paper-track")
   
   # Import core modules
   from src.core.grid import Grid, Task
   from src.dsl import primitives as dsl
   from src.solvers.symbolic_search import SymbolicSearchSolver
   from src.evaluator.verifier import TaskVerifier
   
   print("✓ ARC Dual-System Solver Loaded Successfully!")
   ```
6. Jalankan sel notebook untuk memastikan tidak ada error.
7. Di kanan atas, klik **Save Version** $\to$ pilih **Save & Run All (Commit)** $\to$ klik **Save**.
8. Setelah selesai, buka menu **Share** di kanan atas notebook $\to$ ubah visibilitas menjadi **Public** $\to$ klik **Save**.
9. **Salin URL Notebook Publik Anda** (misal: `https://www.kaggle.com/amansegavo/arc-prize-2026-dual-system-solver`).

---

## 📝 Langkah 2: Submit Write-Up di Halaman Kompetisi Paper Track

1. Buka halaman kompetisi:  
   👉 [https://www.kaggle.com/competitions/arc-prize-2026-paper-track](https://www.kaggle.com/competitions/arc-prize-2026-paper-track)
2. Klik tombol **Submit Writeup** (atau tab *Discussion* / *Submissions*).
3. Isi formulir pengajuan:

### A. Judul Write-up (*Title*):
```
Dual-System Neuro-Symbolic Program Synthesis with Test-Time Verification for ARC-AGI-2
```

### B. Konten Write-up (*Body*):
Salin seluruh teks Markdown dari file [paper_draft_static_grid_reasoning.md](file:///d:/ARC%20Prize%202026%20-%20Paper%20Track/paper_draft_static_grid_reasoning.md).  
*(Teks ini sudah diformat rapi, memiliki rumus matematis, diagram arsitektur, tabel empiris, dan panjangnya di bawah 1.500 kata).*

### C. Media Gallery (Cover Image - Wajib):
Unggah salah satu gambar dari dashboard/arsitektur, misalnya:
- Screenshot Dashboard: `dashboard_loaded_1786884252890.png`
- Visualisasi Task ARC: `task_enclosed_fill_loaded_1786884291348.png`

### D. Project Links (Tautan Proyek):
- **Public Notebook:** Masukkan link Kaggle Notebook publik Anda dari Langkah 1.
- **GitHub Repository (Opsional tapi direkomendasikan):**  
  `https://github.com/AmanSegavo/arc-prize-2026-paper-track`
- **Streamlit Live Dashboard (Opsional):**  
  Masukkan URL Streamlit Cloud Anda (misal `https://arc-prize-2026-paper-track.streamlit.app`).

### E. Tautkan ke Submission Kode ARC-AGI-2:
Pilih submission kode Anda di track prediksi ARC-AGI-2.

4. Klik **Publish Writeup**.

---

## ✅ Checklist Sebelum Deadline 9 November 2026

- [x] Repositori GitHub telah terupload ke `https://github.com/AmanSegavo/arc-prize-2026-paper-track`.
- [x] Draf paper telah memuat nama Author **Abdurrahman Assegaf**.
- [x] Hasil pengujian empiris (400 train, 400 eval) telah dimasukkan ke dalam paper.
- [ ] Notebook Kaggle telah dibuat dan diset menjadi **Public**.
- [ ] Cover image telah diunggah pada Media Gallery.
- [ ] Write-up telah dipublikasikan di kompetisi Paper Track.
