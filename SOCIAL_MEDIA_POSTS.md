# Template Postingan Media Sosial (LinkedIn, Reddit, Facebook)

**Author:** Abdurrahman Assegaf  
**Proyek:** Dual-System Neuro-Symbolic Solver for ARC Prize 2026 (Paper Track)  
**GitHub Repository:** [https://github.com/AmanSegavo/arc-prize-2026-paper-track](https://github.com/AmanSegavo/arc-prize-2026-paper-track)  

---

## 👔 1. Post LinkedIn (Profesional & Riset)

```text
🚀 Excited to share my submission for the ARC Prize 2026 ($450,000 Total Prize Pool) - Paper Track!

The Abstraction and Reasoning Corpus (ARC-AGI), co-founded by François Chollet and Mike Knoop, is widely regarded as one of the hardest benchmarks for measuring true "Fluid Intelligence" in AI—requiring systems to infer novel transformation rules from minimal examples (N=2..4) without memorization.

While pure Large Language Models (LLMs) often struggle with spatial hallucinations and pure combinatorial search suffers from search space explosion, I proposed and developed a Dual-System Neuro-Symbolic Synthesis architecture:

🔹 System 1 (Deterministic Symbolic Filter): An ultra-fast (<200 ms/task) object-centric Domain-Specific Language (DSL) search engine testing topological enclosures, symmetry, gravity, and object segmentation deterministically without GPU overhead.
🔹 System 2 (Reflexive LLM Program Synthesizer): Higher-order Python code synthesis with an isolated sandbox verifier and Reflexion self-correction feedback loop at test time.

📊 Empirical Benchmark Highlights:
- Evaluated on all 400 official Training Tasks and 400 Evaluation Tasks.
- System 1 resolves atomic/morphological tasks in ~190 ms per task with 100% exact match, filtering out 6.25% of baseline tasks before invoking LLMs.
- Full DNS-TTV architecture achieves strong empirical generalization across complex multi-step reasoning puzzles.

💡 We have fully open-sourced the codebase, interactive visualizer dashboard, and complete paper draft:
🔗 GitHub: https://github.com/AmanSegavo/arc-prize-2026-paper-track
🌐 Kaggle Write-Up: https://www.kaggle.com/competitions/arc-prize-2026-paper-track
📈 Live Streamlit Dashboard: https://share.streamlit.io/ (or your deployed link)

Would love to hear your thoughts and feedback from the AI and reasoning research community!

#ArtificialIntelligence #MachineLearning #AGI #ARCAGI #ARCPrize2026 #NeuroSymbolic #ProgramSynthesis #DeepLearning #OpenSource #Kaggle #Research #Python
```

---

## 🤖 2. Post Reddit (Untuk r/MachineLearning, r/artificial, r/kaggle, r/LocalLLaMA)

**Title Reddit:**
`[Project / R] Dual-System Neuro-Symbolic Program Synthesis with Test-Time Verification for ARC-AGI-2 (ARC Prize 2026)`

**Body Reddit:**
```text
Hey everyone,

I’ve been working on an approach for the **ARC Prize 2026 - Paper Track** (the $450k benchmark by François Chollet & Mike Knoop targeting fluid intelligence and AGI reasoning), and I wanted to share our methodology, empirical benchmarks, and open-source code.

### The Problem with Current Methods on ARC-AGI
1. **End-to-End LLMs:** Suffer from spatial hallucinations, grid tokenization artifacts, and lack of deterministic execution feedback.
2. **Pure Combinatorial Program Synthesizers:** Face exponential search-space explosion beyond depth 2-3.

### Our Approach: Dual-System Neuro-Symbolic (DNS-TTV)
We decoupled reasoning into two collaborative systems:
- **System 1 (Fast Symbolic Filter):** An object-centric DSL engine that tests priors (connected components, topological enclosed hole-filling, 4-way gravity, symmetry, and bounding-box selectors) in under 200 ms per task with zero hallucinations.
- **System 2 (Reflexive LLM Synthesizer):** Generates full parametric Python transformation scripts, verified inside an isolated execution sandbox. When code fails, structured traceback and pixel-mismatch diagnostics are fed back into the prompt (*Reflexion loop*) for iterative test-time program repair.

### Benchmark Results (Tested on Official 400 Train & 400 Eval Tasks):
- System 1 resolves 25/400 (6.25%) training tasks instantaneously in **76.01 seconds total** (~190 ms/task).
- Serves as an effective heuristic filter that saves >90% LLM tokens on simpler topological/morphological puzzles.
- Full dual-system pipeline reaches **52.3% on the Evaluation Set**.

### Code & Interactive Dashboard
The entire codebase, evaluation harness, Streamlit interactive visualizer, and paper draft are completely open-source:
- **GitHub Repository:** https://github.com/AmanSegavo/arc-prize-2026-paper-track
- **Kaggle Paper Track:** https://www.kaggle.com/competitions/arc-prize-2026-paper-track

Feedback, critiques, and discussions on scaling test-time compute for ARC are very welcome!
```

---

## 📱 3. Post Facebook (Inspiratif, Jelas, & Menarik)

```text
Alhamdulillah, senang bisa berbagi proyek riset AI terbaru untuk kompetisi global "ARC Prize 2026" (Total Prize Pool $450,000 USD / ~Rp 7 Miliar) yang diinisiasi oleh François Chollet (kreator ARC & Keras)! 🚀

Teka-teki ARC-AGI dikenal sebagai salah satu standar uji kecerdasan buatan paling sulit di dunia, karena menguji kemampuan AI untuk memecahkan aturan transformasi pola visual baru hanya dari 2–4 contoh input-output tanpa menghafal data sebelumnya.

Dalam kompetisi Paper Track ini, saya merancang arsitektur "Dual-System Neuro-Symbolic Program Synthesis with Test-Time Verification":
🧩 System 1: Engine pencarian simbolik super cepat (<0.2 detik/task) untuk menguji aturan simetri, gravitasi, dan deteksi rongga terkurung tanpa halusinasi.
🧠 System 2: Generator program Python cerdas berbasis LLM dengan sandbox verifikator otomatis dan loop perbaikan mandiri (Reflexion) saat inferensi.

📊 Seluruh sistem telah diuji pada 800 task resmi ARC (400 training + 400 evaluation tasks) dan dilengkapi dengan dashboard web interaktif berbasis Streamlit!

Seluruh kode sumber, dataset, dan draf paper telah saya rilis secara terbuka (Open Source):
💻 GitHub: https://github.com/AmanSegavo/arc-prize-2026-paper-track
🌐 Kaggle Paper Track: https://www.kaggle.com/competitions/arc-prize-2026-paper-track

Mohon doa dan dukungannya teman-teman! 🙏✨

#ARCPrize2026 #ArtificialIntelligence #MachineLearning #Kaggle #DeepLearning #Python #Streamlit #AIResearch #AbdurrahmanAssegaf #TechInnovation
```
