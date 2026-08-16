# Panduan Mendalam Rubrik Evaluasi & Filosofi Penilaian ARC Prize 2026

Untuk memenangkan penghargaan utama dan menembus skor $\ge 4.5 / 5.0$ pada Paper Track (sehingga berhak atas bagian dari **Bonus Pool $375,000**), penting untuk memahami filosofi inti dari François Chollet dan Mike Knoop mengenai ARC-AGI dan kecerdasan artifisial.

---

## 🧠 1. Filosofi Inti: Definisi Kecerdasan menurut François Chollet

Dalam papernya *"On the Measure of Intelligence"* (Chollet, 2019), kecerdasan didefinisikan sebagai:
> **"The efficiency of an information-processing system with respect to its ability to acquire new skills over a scope of tasks with respect to priors, experience, and generalization difficulty."**
> *(Efisiensi suatu sistem dalam memperoleh keterampilan baru untuk berbagai tugas, relatif terhadap pengetahuan awal/priors, pengalaman, dan tingkat kesulitan generalisasi).*

### Apa yang BUKAN Diinginkan:
- ❌ **Pure Memorization / Vast Pre-training Brute-force:** Melatih LLM dengan triliunan token atau menghafal jutaan variasi grid puzzle tanpa mekanisme penalaran terstruktur.
- ❌ **Hardcoded Heuristics:** Kumpulan aturan if-else manual yang hanya bekerja pada 2-3 soal tertentu namun gagal ketika dimensi atau warna diubah sedikit.
- ❌ **Expensive Inefficient Scaling:** Menggunakan ratusan GPU hanya untuk menebak secara acak jutaan kali tanpa pemodelan kausal atau verifikasi hipotesis.

### Apa yang SANGAT Diinginkan:
- ✅ **Sample-efficient Generalization:** Mampu memecahkan tugas dari 2–4 contoh (*few-shot demonstration*) secara tepat.
- ✅ **Dynamic Program Synthesis / Search:** Membentuk program simbolik atau representasi diskret yang memverifikasi solusi terhadap contoh input-output.
- ✅ **Adaptive World-Modeling:** (Khususnya di ARC-AGI-3) Agen yang mampu bereksplorasi secara efisien untuk membangun peta aturan dunia tersembunyi (*hidden rules*).
- ✅ **Mechanistic Understanding:** Penjelasan matematis atau arsitektural mengapa pendekatan tersebut mampu melakukan generalisasi (*fluid reasoning*).

---

## 🎯 2. Analisis 6 Dimensi Rubrik Penilaian

### 1. Accuracy (Akurasi & Performa Leaderboard)
- **Target Skor 5:** Hasil submission kode yang ditautkan mencapai performa tinggi di public/private leaderboard (misal $\ge 40-70\%$ pada ARC-AGI-2 atau efisiensi aksi tinggi di ARC-AGI-3).
- **Strategi Penulisan:** 
  - Tampilkan tabel komparasi hasil yang jelas (Train split, Evaluation split, Private test bila tersedia).
  - Tunjukkan confidence intervals dan perbandingan dengan baseline standar (Direct LLM Prompting, Dreamer, DSL Synthesis, dll.).

### 2. Universality (Universalitas & Transferabilitas)
- **Target Skor 5:** Pendekatan tidak *overfitted* ke format grid 2D semata, melainkan merupakan kerangka kerja umum (*general reasoning framework*) yang dapat diterapkan pada pemecahan masalah simbolik, planning, causal inference, atau general code generation.
- **Strategi Penulisan:**
  - Jelaskan bagaimana abstraksi inti (misal: hypothesis generation, test-time verifier, search tree guidance) dapat digeneralisasikan ke domain lain.
  - Berikan diskusi konseptual tentang batasan domain dan potensi perluasan.

### 3. Progress (Kontribusi Menuju Target 85% ARC-AGI)
- **Target Skor 5:** Memberikan fondasi atau arah baru yang meyakinkan para juri bahwa "jika arah riset ini dikembangkan lebih lanjut, komunitas AI akan mampu mencapai 85% akurasi pada ARC-AGI".
- **Strategi Penulisan:**
  - Diskusikan *scaling laws* dari metode Anda: Apakah performanya meningkat secara efisien dengan penambahan *test-time compute* atau search depth yang lebih pintar?
  - Analisis *gap analysis*: Apa yang saat ini belum bisa diselesaikan dan bagaimana roadmap untuk menutup gap tersebut?

### 4. Theory (Landasan Teori & Analisis 'Why It Works')
- **Target Skor 5:** Paper tidak hanya mendeskripsikan langkah-langkah implementasi, tetapi memberikan wawasan teoretis/matematis yang kuat mengapa representasi atau algoritma pencarian tersebut optimal.
- **Strategi Penulisan:**
  - Sajikan formulasi formal (misal: Bayesian Program Learning, Minimal Description Length / Occam's Razor, Markov Decision Process untuk interaksi di ARC-AGI-3).
  - Jelaskan mekanisme representasi: Bagaimana konsep objek, topologi, simetri, dan transformasi direpresentasikan dalam ruang laten atau DSL (*Domain-Specific Language*).

### 5. Completeness (Kelengkapan, Studi Ablasi, & Reproducibility)
- **Target Skor 5:** Dokumentasi sangat komprehensif, mencakup diagram arsitektur lengkap, tabel ablation study yang mengisolasi kontribusi setiap komponen, analisis kegagalan (*failure case analysis*), dan instruksi reproduksi yang jelas.
- **Strategi Penulisan:**
  - Sertakan diagram alur data/algoritma yang elegan.
  - Sediakan tabel ablasi: "Performa tanpa komponen X, tanpa search Y, tanpa verification Z".
  - Bahas secara transparan 3–4 kasus di mana sistem gagal dan mengapa.

### 6. Novelty (Orisinalitas & Kebaruan)
- **Target Skor 5:** Mengajukan paradigma baru yang berbeda secara signifikan dari solusi umum (misal: kombinasi baru antara Neuro-symbolic synthesis + active world model, dynamic DSL creation, atau search-guided latent planning).
- **Strategi Penulisan:**
  - Bandingkan secara eksplisit dengan metode mutakhir sebelumnya (misal: Ryan Greenblatt's GPT-4o fine-tuning + test-time search, MindsAI DSL synthesizer, Jack Cole's test-time training).
  - Tunjukkan diferensiasi unik arsitektur Anda.

---

## ⏱️ 3. Checklist Penting Sebelum Submit

- [ ] Kode submission ARC-AGI-2 atau ARC-AGI-3 sudah berjalan dan menghasilkan skor yang valid di Kaggle.
- [ ] Notebook publik sudah dibuat dan ditautkan di write-up (`Project Links`).
- [ ] Gambar cover yang menarik dan profesional diunggah di `Media Gallery`.
- [ ] Jumlah kata di badan write-up tidak melebihi **1.500 kata**.
- [ ] Seluruh diagram dan tabel memiliki keterangan yang jelas.
- [ ] Paper PDF versi panjang (opsional namun direkomendasikan) di-host di GitHub/arXiv dan ditautkan.
- [ ] Lisensi kode diset ke open source permisif (CC-BY-4.0 / MIT / Apache-2.0).
