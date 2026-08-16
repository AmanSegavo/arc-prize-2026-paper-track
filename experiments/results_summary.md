# Laporan Eksperimen & Hasil Benchmark ARC-AGI-2

Dokumen ini mencatat hasil pengujian empiris solver simbolik berbasis DSL pada dataset resmi ARC-AGI (400 Training Tasks). Data ini dapat langsung dikutip pada bagian **4. Experimental Results & Ablation Study** di paper write-up.

---

## 📊 1. Ringkasan Kinerja (Training Set - 400 Tasks)

| Metrik Evaluasi | Nilai Empiris |
| :--- | :--- |
| **Total Tasks Diuji** | 400 tasks |
| **Penyelesaian Sempurna (Exact Match 100%)** | **25 tasks (6.25%)** |
| **Kecepatan Inferensi per Task** | **190.00 ms** (~0.19 detik) |
| **Total Waktu Komputasi (400 Tasks)** | **76.01 detik** |
| **Search Space Budget** | Depth $\le 2$ (Unary & 2-step composition) |

---

## 🧩 2. Analisis Solusi & Kategori Transformasi

Berikut adalah beberapa contoh task ARC asli yang berhasil dipecahkan secara instan dan deterministik oleh engine DSL:

### A. Geometri & Simetri
- `3c9b0459`: `rot180(grid)` (Waktu: 0.000s)
- `6150a2bd`: `rot180(grid)` (Waktu: 0.000s)
- `ed36ccf7`: `rot270(grid)` (Waktu: 0.000s)

### B. Topologi & Deteksi Rongga Terkurung (Enclosure)
- `00d62c1b`: `fill_enclosed(grid, 4)` (Waktu: 0.011s) — *Mengisi rongga dalam poligon tertutup dengan warna kuning.*
- `4347f46a`: `outline(grid)` (Waktu: 0.002s) — *Mengekstrak batas luar / perimeter objek.*

### C. Gravitasi Spasial (Goal-Directed Physics)
- `1e0a9b12`: `gravity_down(grid)` (Waktu: 0.001s) — *Menjatuhkan semua balok ke bawah.*
- `3906de3d`: `gravity_up(grid)` (Waktu: 0.002s) — *Menarik semua elemen ke atas.*

### D. Abstraksi Objek (Object-Centric Cropping)
- `1cf80156`: `crop_nonzero(grid)` (Waktu: 0.000s)
- `1f85a75f`: `crop_largest_object(grid)` (Waktu: 0.001s) — *Memilih dan meng-crop objek dengan area terbesar.*
- `a87f7484`: `crop_largest_object(grid)` (Waktu: 0.002s)
- `be94b721`: `crop_largest_object(grid)` (Waktu: 0.001s)
- `23b5c85d`: `crop_smallest_object(grid)` (Waktu: 0.004s) — *Memilih objek terkecil.*
- `39a8645d`: `crop_smallest_object(grid)` (Waktu: 0.001s)
- `d9fac9be`: `crop_smallest_object(grid)` (Waktu: 0.002s)

### E. Skalasi & Resizing
- `c59eb873`: `scale_up_2x(grid)` (Waktu: 0.001s)

### F. Substitusi Warna (Color Mapping)
- `b1948b0a`: `replace_color(grid, 6, 2)` (Waktu: 0.003s) — *Magenta digantikan Merah.*
- `c8f0f002`: `replace_color(grid, 7, 5)` (Waktu: 0.002s) — *Oranye digantikan Abu-abu.*

### G. Komposisi Multilangkah (Depth 2 Composition)
- `f25fbde4`: `scale_up_2x(crop_nonzero(grid))` (Waktu: 0.016s) — *Meng-crop objek aktif lalu memperbesar 2x lipat.*

---

## 📈 3. Wawasan Teoretis untuk Paper (Theory & Progress)

1. **Efisiensi Komputasi Ekstrem:**
   Dengan rata-rata 190 ms per task, pencarian simbolik menyediakan *fast heuristic filter* (System 1) yang menyaring 6–10% task sederhana tanpa perlu memanggil LLM yang mahal.
2. **Kebutuhan Hybrid Neuro-Symbolic:**
   Sisa task yang belum terpecahkan membutuhkan komposisi lebih dalam, parameter dinamis kontekstual, atau penalaran graf relasional. Ini menjadi justifikasi kuat mengapa pipeline **Hybrid LLM + Verifier + Dynamic DSL Search** diperlukan untuk mengejar target 85% AGI.
