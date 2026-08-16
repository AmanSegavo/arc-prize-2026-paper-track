# Panduan Lengkap Penalaran Grid Statis (ARC-AGI-2)

Dokumen ini adalah cetak biru teknis dan metodologis untuk merancang sistem **Penalaran Grid Statis (Static Grid Reasoning)** serta menyusun paper yang kompetitif untuk **ARC Prize 2026 - Paper Track**.

---

## 🧩 1. Karakteristik & Tantangan ARC-AGI-2

ARC-AGI-2 berfokus pada penalaran induktif dari 2–4 pasangan contoh input-output ($X_{\text{train}} \to Y_{\text{train}}$) untuk memprediksi output dari grid uji baru ($X_{\text{test}} \to Y_{\text{test}}$).

### 4 Priors Inti (*Core Knowledge Priors*) yang Diuji:
1. **Objectness (Keberadaan Objek):**
   - Piksel-piksel terhubung dengan warna seragam membentuk objek tunggal (*Connected Components*).
   - Objek memiliki batas (*boundaries*), persistensi (*object persistence*), dan kontinuitas bentuk.
2. **Goal-Directedness & Agency:**
   - Objek dapat bergerak, saling bertumbukan (*collision*), jatuh mengikuti gravitasi, atau menyejajarkan diri (*alignment*).
3. **Geometry & Topology:**
   - Simetri, rotasi (90°, 180°, 270°), refleksi horizontal/vertikal, translasi, skalasi, rongga tertutup (*enclosures*), lubang (*holes*).
4. **Numbers & Counting:**
   - Menghitung jumlah objek, mengurutkan berdasarkan ukuran (*area*), warna mayoritas vs minoritas, pengulangan periodik (*tiling*).

---

## 🏗️ 2. Arsitektur Pipeline yang Telah Dibangun

Framework yang telah diimplementasikan dalam repositori ini:

```
d:\ARC Prize 2026 - Paper Track\
├── src\
│   ├── core\
│   │   └── grid.py            # Abstraksi Grid, Object, Connected Components, Task loader
│   ├── dsl\
│   │   └── primitives.py      # Primitif transformasi (Geometri, Warna, Gravitasi, Topologi)
│   ├── evaluator\
│   │   └── verifier.py        # TaskVerifier & Execution Sandbox (menguji kandidat program)
│   ├── solvers\
│   │   ├── symbolic_search.py # Solver pencarian kombinatorial DSL & A*
│   │   └── llm_synthesizer.py # LLM Code Generation dengan Reflexion / Self-Correction
│   └── __init__.py
├── tests\
│   └── test_pipeline.py       # Unit tests validasi pipeline
├── paper_template.md          # Template write-up Kaggle (< 1500 kata)
├── paper_guidelines_and_rubric.md # Panduan skor 4.5+ rubrik
└── README.md
```

---

## 🔬 3. Strategi Penelitian untuk Paper Track ARC-AGI-2

Agar paper Anda menembus skor $\ge 4.5$ pada rubrik evaluasi:

### A. Teori (*Theory*) & Universalitas (*Universality*)
- Formulasikan ARC sebagai masalah **Bayesian Program Learning (BPL)** atau **Minimum Description Length (MDL)**:
  $$\hat{P} = \arg\min_{P \in \mathcal{H}} \left( \text{Length}(P) + \lambda \sum_{i} \mathcal{L}(P(X_i), Y_i) \right)$$
- Jelaskan bahwa sistem tidak sekadar mencocokkan pola piksel, melainkan membangun hipotesis aturan (*rule induction*) yang dapat diverifikasi secara deterministik.

### B. Studi Ablasi (*Ablation Study*)
Buktikan kontribusi masing-masing komponen dalam paper:
1. *Baseline*: LLM zero-shot tanpa eksekutor sandbox.
2. *+ Execution Sandbox & Verifier*: LLM + verifikasi pada training examples.
3. *+ Reflexion Loop*: LLM yang memperbaiki kodenya sendiri berdasarkan pesan kegagalan (*error traceback*).
4. *+ Object-Centric DSL Primitives*: Membantu LLM/Search engine dengan fungsi tingkat tinggi (misal: `crop_nonzero`, `fill_enclosed`, `apply_gravity`).

### C. Analisis Kasus Gagal (*Failure Modes*)
Juri (François Chollet) sangat menyukai analisis yang jujur dan mendalam mengenai batas kemampuan model:
- **Topology Ambiguity**: Kapan suatu pola memiliki lebih dari satu interpretasi yang valid?
- **Search Space Explosion**: Kapan kedalaman transformasi rekursif membuat pencarian tidak feasible dalam batas waktu inferensi?
