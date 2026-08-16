# Template Write-Up: ARC Prize 2026 Paper Track
*(Batas maksimal 1.500 kata untuk platform Kaggle Writeup)*

---

# [Judul Paper yang Kuat dan Deskriptif: misal *Neuro-Symbolic Active Hypothesis Search for ARC-AGI-2/3*]

**Penulis:** [Nama Tim / Anggota]  
**Track Terkait:** [ARC-AGI-2 (Static Reasoning) / ARC-AGI-3 (Interactive Agents)]  
**Link Notebook Publik:** [URL Kaggle Public Notebook]  
**Link Repository / PDF Lengkap (Opsional):** [URL GitHub / arXiv]  

---

## 1. Abstract & Executive Summary (~150 kata)
*Ringkasan singkat tentang masalah, pendekatan konseptual yang diajukan, hasil utama, dan kontribusi terhadap kemajuan AGI.*
- **Problem:** Keterbatasan pendekatan saat ini (misal: LLM hallucination pada penalaran spasial atau search space explosion pada pure DSL program synthesis).
- **Core Proposal:** Arsitektur yang memadukan [misal: Neuro-symbolic abstraction, active exploration, dynamic DSL pruning, test-time tree search with execution feedback].
- **Key Results:** Mencapai [X]% akurasi pada Evaluation Set dengan latensi [Y] detik/tugas.

---

## 2. Motivation & Theoretical Formulation (~250 kata)
*Menjawab dimensi: **Theory** & **Universality***
- **Core Intuition:** Mengapa metode ini dirancang seperti ini? Apa representasi matematis atau komputasi dari 'abstraksi' yang digunakan?
- **Formal Definition:**
  - Definisikan ruang hipotesis $\mathcal{H}$, fungsi evaluasi/verifikasi $V(h, D_{\text{train}})$, dan fungsi seleksi $P(h | D_{\text{train}})$.
  - Hubungan dengan prinsip kompresi data (*Minimum Description Length* / *Bayesian Program Learning*).
- **Universality:** Mengapa prinsip ini tidak hanya berlaku untuk grid puzzle, tetapi juga untuk penalaran berbasis aturan (*rule-induction*) pada umumnya.

---

## 3. System Architecture & Methodology (~350 kata)
*Menjawab dimensi: **Completeness** & **Novelty***

```
[ Diagram Arsitektur / Pipeline Flowchart ]
Contoh Alur:
Input Task Examples -> Object-Centric Decomposition -> Hypothesis / Code Generator (Policy) 
  -> Sandbox Executor & Verifier -> Test-Time Search / MCTS -> Output Prediction
```

Jelaskan komponen utama:
1. **Perception & Object Decomposition:** Bagaimana input grid atau state interaktif diparse menjadi entitas diskret (objek, konektivitas, warna, simetri).
2. **Hypothesis Generation Engine:** Mekanisme pembentukan program atau rencana (misal: Fine-tuned LLM, Domain-Specific Language, Graph Transformation).
3. **Execution Sandbox & Verification:** Verifikasi terhadap contoh training.
4. **Test-Time Search / Optimization:** Algoritma pencarian (misal: Monte Carlo Tree Search, Beam Search, Reflexion/Self-Correction).

---

## 4. Experimental Results & Ablation Study (~300 kata)
*Menjawab dimensi: **Accuracy** & **Completeness***

### 4.1 Benchmark Performance
| Split / Setup | Baseline (e.g. GPT-4o Zero-Shot) | Previous SOTA | **Metode Kami** |
| :--- | :---: | :---: | :---: |
| **ARC Training Set (400 tasks)** | 35.0% | 72.0% | **84.5%** |
| **ARC Evaluation Set (400 tasks)** | 22.0% | 45.0% | **58.2%** |
| **Private Leaderboard Score** | - | - | **[Score Anda]** |

### 4.2 Ablation Study (Menguji Kontribusi Tiap Modul)
| Variasi Konfigurasi | Akurasi (%) | Rata-rata Token / Waktu per Task |
| :--- | :---: | :---: |
| Full Proposed Pipeline | **58.2%** | 4.2s |
| *w/o Test-Time Verification* | 34.1% | 1.1s |
| *w/o Object-Centric DSL* | 29.5% | 8.9s |
| *w/o Dynamic Self-Correction* | 44.8% | 2.5s |

---

## 5. Failure Modes & Qualitative Analysis (~200 kata)
*Menjawab dimensi: **Completeness** & **Theory***
- **Analisis Kasus Gagal (Failure Cases):**
  - Kasus 1: *Complex Topology / Fractal recursion* — Mengapa sistem gagal (misal: kedalaman rekursi melampaui search budget).
  - Kasus 2: *Ambiguous Multi-rule Tasks* — Kegagalan memilih hipotesis paling sederhana ketika ada meerdere solusi valid.
- Sertakan 1–2 visualisasi perbandingan antara prediksi sistem vs *ground truth*.

---

## 6. Discussion, Scaling Laws, & Path to 85% AGI (~200 kata)
*Menjawab dimensi: **Progress** & **Universality***
- **Test-Time Scaling:** Bagaimana performa meningkat seiring penambahan komputasi inferensi (*compute-accuracy trade-off*).
- **Roadmap to 85%:** Apa 2–3 terobosan yang masih dibutuhkan untuk mencapai ambang batas 85% (misal: learned visual priors, persistent memory in ARC-AGI-3, open-ended curriculum learning).
- **Kesimpulan:** Ringkasan kontribusi utama terhadap lanskap riset Artificial General Intelligence.

---

## 7. Open-Source & Reproducibility
- Kode sumber lengkap dilisensikan di bawah CC-BY-4.0.
- Link ke Kaggle Public Notebook: [Link]
- Dependensi dan instruksi instalasi dapat dilihat pada notebook.
