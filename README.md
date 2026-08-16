# ARC Prize 2026 - Paper Track: Panduan Lengkap & Strategi Kompetisi

Repository ini berisi ringkasan komprehensif, panduan teknis, template penulisan, dan analisis strategi untuk **ARC Prize 2026 - Paper Track** di Kaggle.

---

## 📌 Ringkasan Kompetisi

- **Nama Kompetisi:** ARC Prize 2026 - Paper Track
- **URL Kaggle:** [https://www.kaggle.com/competitions/arc-prize-2026-paper-track](https://www.kaggle.com/competitions/arc-prize-2026-paper-track)
- **Host / Juri:** François Chollet (`@fchollet`) & Mike Knoop (`@mikeknoop`)
- **Total Hadiah:** **$450,000 USD**
  - **Main Track Awards ($75,000):**
    - 🥇 Juara 1: **$50,000**
    - 🥈 Juara 2: **$20,000**
    - 🥉 Juara 3: **$5,000**
  - **Outstanding Papers Bonus Pool ($375,000):**
    - Dibagikan merata ke paper yang memperoleh skor rubrik $\ge 4.5 / 5.0$.
- **Jadwal Penting:**
  - **Mulai:** 25 Maret 2026
  - **Deadline Final Submission:** **9 November 2026 (23:59 UTC)**

---

## 🎯 Tujuan & Esensi Paper Track

ARC Prize Paper Track dirancang untuk mendokumentasikan dan memberi penghargaan pada **kemajuan konseptual (conceptual breakthroughs)** dalam memecahkan ARC-AGI. Tujuan utamanya bukan sekadar mendapatkan skor tertinggi melalui bruteforce atau heuristic rapuh, melainkan memahami **mengapa dan bagaimana** suatu pendekatan dapat menghasilkan kecerdasan fluida (*fluid intelligence*) dan kemampuan adaptasi terhadap pola baru (*novel generalization*).

### ⚠️ Syarat Wajib Keterkaitan (Linked Submission)
Untuk memenuhi syarat di Paper Track:
1. Paper / Write-up **wajib ditautkan (linked)** ke sebuah submission kode aktif di salah satu dari dua track prediksi:
   - **ARC-AGI-2:** Track reasoning statis (grid-based transformation).
   - **ARC-AGI-3:** Track reasoning interaktif (agentic exploration & adaptation in dynamic environments).
2. Kode submission tidak harus menduduki peringkat #1 di leaderboard, tetapi harus berupa sistem yang valid, nyata, dan dapat direproduksi.

---

## 📊 Rubrik Evaluasi Paper (Skala 0 - 5)

Penilaian dilakukan secara holistik dengan merata-ratakan skor dari 6 dimensi:

| Dimensi | Bobot Penjelasan | Fokus Pertanyaan Juri |
| :--- | :--- | :--- |
| **1. Accuracy** | Performa Leaderboard | Seberapa tinggi skor submission terkait di private/public leaderboard? |
| **2. Universality** | Generalisasi Luas | Seberapa universal metode ini di luar task ARC spesifik? Apakah prinsipnya dapat diterapkan ke domain penalaran lain? |
| **3. Progress** | Kemajuan Menuju Target | Seberapa besar metode ini meningkatkan peluang komunitas AI mencapai target benchmark $\ge 85\%$ pada ARC-AGI? |
| **4. Theory** | Landasan Teoretis | Mengapa metode ini bekerja (*why it works*), bukan hanya bagaimana menjalankannya (*how it works*)? Apakah ada analisis mekanistik / formal? |
| **5. Completeness** | Kelengkapan & Reproducibility | Apakah paper menjelaskan seluruh alur pipeline, arsitektur, ablation study, batasan (*failure modes*), dan cara reproduksi secara tuntas? |
| **6. Novelty** | Kebaruan Konseptual | Seberapa orisinal dan inovatif ide yang diajukan dibandingkan riset publik yang sudah ada? |

---

## 📝 Format & Persyaratan Submission

1. **Format:** Kaggle Writeup Platform (Kaggle Discussion / Competition Writeup Interface).
2. **Batas Kata:** **Maksimal 1.500 kata** pada write-up utama.
3. **Aset Wajib:**
   - **Cover Image:** Wajib diunggah pada Media Gallery write-up.
   - **Public Notebook Link:** Wajib ditautkan pada field Project Links (harus berstatus publik).
   - *(Opsional namun sangat disarankan)*: Link PDF Paper Lengkap (misal di GitHub/arXiv) atau visualisasi interaktif.
4. **Lisensi:** Lisensi terbuka (CC-BY-4.0 untuk code pemenang / open source permisif).
5. **Tie Breaker:** Jika terjadi nilai seri pada rubrik, prioritas diberikan kepada yang melakukan submit lebih awal.

---

## 📂 Struktur Dokumen Panduan

1. 📄 [`paper_guidelines_and_rubric.md`](./paper_guidelines_and_rubric.md) — Panduan mendalam tentang 6 kriteria rubrik evaluasi dan strategi memaksimalkan skor.
2. 📝 [`paper_template.md`](./paper_template.md) — Template writeup terstruktur $\le 1500$ kata siap pakai.
3. 🧠 [`arc_prize_2026_strategies.md`](./arc_prize_2026_strategies.md) — Tinjauan arsitektur state-of-the-art (Program Synthesis, Test-Time Search, LLM Fine-Tuning, Object-Centric Representations, Interactive RL).
