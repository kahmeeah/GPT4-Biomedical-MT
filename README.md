# Biomedical Translation with GPT-4-Turbo ![ChatGPT Icon](https://img.icons8.com/?size=25&id=FBO05Dys9QCg&format=png&color=000000)

This repository contains the code and data used for the research paper:  
**"Assessing the Efficacy of GPT-4 in the Sentence-Level Translation of Medical Abstracts: A Comparative Study"**  

The full report is available to download.

[![Download PDF](https://img.shields.io/badge/Download-PDF-red?style=flat&logo=adobe-acrobat-reader)](https://github.com/kahmeeah/GPT4-Biomedical-MT/raw/main/gpt4_biomedical_mt_2024.pdf)

## Overview

This project evaluates GPT-4-Turbo's performance in translating biomedical abstracts across 12 language pairs. The study compares GPT-4-Turbo with commercial translation systems such as Google Translate and DeepL, utilizing the **Biomedical Multidimensional Quality Metrics (MQM) Dataset.**  

**Key Highlights:**  
- Evaluates translation quality using automatic metrics: **BLEU, CHRF++, and TER.**  
- Translations performed using APIs for **GPT-4, Google Translate, and DeepL.**  
- Human evaluation conducted for Pt ⇒ En translations.

## Contributors
- [Ana Pacheco](https://github.com/anaspacheco)
- [Kahmeeah Obey](https://github.com/kahmeeah)
- [James Li](https://github.com/j4mesli)
- Nicole Luzuriaga

---

## Project Structure
- `src/main.py` – Main script to run the translation pipeline.
- `src/evaluation.py` – Handles automated evaluation using BLEU, CHRF++, and TER metrics.
- `src/translation.py` – Manages the core translation logic and calls apropiate API functions.
- `src/utils/api_utils.py` – Manages API requests for translation services (GPT-4, Google, DeepL).
- `alignment_files/` – Contains data used for aligning parallel translation texts.
- `evaluation_files/` – Stores evaluation reports and analysis results.
- `parallel_files/` – Holds the bilingual text pairs used for translation testing.
- `result_files/` – Stores translated files generated by each API.

## Installation & Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/kahmeeah/GPT4-Biomedical-MT.git
    cd GPT4-Biomedical-MT
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure APIs in a ```.env``` file:
   ```bash
   PROJECT_ID=your_key # google translate project id
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/file.json
   GOOGLE_key=your_key
   DEEPL_AUTH_KEY=your_key
   OPENAI_KEY=your_key
   OPENAI_MODEL=your_model
   ```

5. Run the program:
    ```bash
    python main.py
    ```

---
## Results

The study found that GPT-4-Turbo demonstrates strong potential for biomedical translations but lags behind specialized NMT systems in some language pairs. Further manual evaluation is recommended for more conclusive findings.

For a detailed analysis, refer to our research paper.

---

## Citation
If you find this project useful, please cite our paper:
```ruby
@article{gpt4_biomedical_mt_2024,
  author    = {Ana Pacheco and Kahmeeah Obey and Nicole Luzuriaga and James Li},
  title     = {Assessing the Efficacy of GPT-4 in the Sentence-Level Translation of Medical Abstracts: A Comparative Study},
  year      = {2024},
  url       = {https://github.com/kahmeeah/GPT4-Biomedical-MT/}
}

```
