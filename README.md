# README.md (Full Version)

# The Authenticity Paradox in Traditional Crafts: Data and Analysis

This repository contains the replication package, including anonymized datasets and Python analysis scripts, for the research paper:

> **"The Authenticity Paradox: Cultural Knowledge Brokers as Mediators of Identity Threat and Psychological Reactance in Traditional Craft Industries"**
> *Authors: Koki Arai and Yuko Oki (2026)*

## 📌 Project Overview

Traditional craft industries face an existential paradox: technological innovation is essential for heritage preservation, yet its adoption often triggers an **identity threat** to the consumer's cultural self-concept. This leads to **psychological reactance**, where consumers resist adoption even when they are aware of the technology's benefits.

Through a convergent mixed-methods design involving 500 consumers and 500 artisans in Japan, this study identifies a "Mediation Gap". We demonstrate that current artisan discourse is heavily biased toward narrative framing, leaving the experiential (visual) needs of consumers unaddressed.

## 📂 Repository Structure

```text
.
├── data/
│   ├── consumer_survey_data.csv    # Anonymized consumer responses (n=500)
│   └── artisan_survey_data.csv     # Anonymized artisan responses (n=500)
├── scripts/
│   └── statistical_analysis.py     # Main analysis script (Chi-square, ANOVA, OLS)
├── requirements.txt                # Python dependency list
├── LICENSE                         # MIT License text
└── README.md                       # This file

```

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher
* All necessary libraries are listed in `requirements.txt`.

### Installation and Execution

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/authenticity-paradox.git
cd authenticity-paradox

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the analysis:**
To reproduce the findings presented in Section 4 of the paper (Awareness-Adoption Paradox, Cluster Analysis, and Mediation Imbalance), execute:
```bash
python scripts/statistical_analysis.py

```



## 📊 Data Description & Measures

Since original survey instruments were not initially designed with psychometric scales, we employ theoretically grounded **proxy measures**:

* 
**Identity Threat (Proxy)**: Measured via a 6-point Likert item assessing "concern about loss of traditional value".


* **Psychological Reactance (Behavioral Proxy)**: Inferred through **Price Tolerance** (5-point scale). Reactance manifests as an unwillingness to pay a premium for products perceived as inauthentic.


* 
**Cultural Identification (Age Proxy)**: Younger cohorts are used as a proxy for heightened identification with tradition as a "scarce cultural resource".


* 
**Mediation Space (Qualitative)**: 2,352 artisan discourse segments coded into Narrative (78.2%), Visual (0.2%), and Economic (17.6%) categories.



## 💰 Funding

This work was supported by **JSPS KAKENHI** (Japan Society for the Promotion of Science):

* Grant Number: **22H00881** 


* Grant Number: **23K01404** 



## ⚖️ License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute the code and data for academic purposes, provided that appropriate credit is given to the original authors. (See the `LICENSE` file for full text).

## ✉️ Contact

For inquiries regarding the methodology or dataset, please contact:
**Koki Arai** - [Your University Profile Link or Email]

