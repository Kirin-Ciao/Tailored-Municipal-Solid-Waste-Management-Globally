# Tailored-Municipal-Solid-Waste-Management-Globally
Reproducible RF-based MSW forecasting & openLCA system models for our Nature Sustainability study on globally tailored waste management.
---

## Table of Contents
1. [Project Highlights](#1-project-highlights)
2. [Repository Overview](#2-repository-overview)
3. [Random-Forest (MSW Forecasting)](#3-random-forest-msw-forecasting)
4. [LCIA Product-System Models](#lcia-product-system-models)
5. [Supplementary Data Mapping](#supplementary-data-mapping)
6. [Road-map](#road-map)
7. [Citing this Repository](#citing-this-repository)
8. [License](#license)
9. [Contact](#contact)

---

## 1  Project Highlights

- **Published Article**  
  Cao, Q.-L., et al. (2025). *Tailoring municipal solid-waste management worldwide through machine-learning projection and life-cycle assessment*. **Nature Sustainability**. DOI: [to be added]  

- **WeChat Official Account**  
  扫码关注我们的公众号：  
  ![WeChat QR](path/to/your-qr-code.png)  

- **Lab Introduction**  
  吉林大学 食物、农业与生物质课题组
  Food, Agriculture & Biomass Research Group, JLU  
  - 网站：[http://your-lab-website.jlu.edu.cn](http://your-lab-website.jlu.edu.cn)  
  - 简介：本课题组由宋俊年教授和杨巍副教授领衔，主要针对可持续食物与农业系统、废弃物资源化与能源化等方向开展研究。  

---

## 2 Repository Overview
| Branch | Key folders / files | Purpose |
|--------|---------------------|---------|
| `main` | `README`, `CITATION.cff`, issue tracker | Entry point |
| `RandomForest-Forecasting` | `Skeleton_code/`, `Trained_models/`, `PRE_code.py`, `Pipeline1.py`, `Pipeline2.py` | 🔮 MSW generation & composition projection |
| `LCIA-models-openLCA` | `Matrix_CSV/` (raw **A/B/C** matrices) <br> `JSON-LD/` (`*.zip` archives) | ♻️ Life-cycle inventory & impact models |

---

## 3  Random-Forest (MSW Forecasting)

RandomForest-Forecasting/  
├── Skeleton_code/            # training scripts (Chinese comments)  
├── Trained_models/           # fraction-specific *.pkl models  
├── PRE_code.py               # loads pickles → produces forecasts  
├── Pipeline1.py / Pipeline2.py   # optional HPO / troubleshooting flows  
└── requirements.txt  

### Quick start  
    git checkout RandomForest-Forecasting  
    pip install -r requirements.txt  
    python PRE_code.py --year 2035 --scenario SSP2 --country CHN  

> `PRE_code.py` expects the corresponding `*.pkl` in **Trained_models/**.  

Historical samples (2010‒2020) and SSP1-5 drivers (2030‒2050) are released as **Supplementary Data Series 1**.

---

## 4  LCIA Product-System Models

Format      | Location                                    | How to use in openLCA 2.0.4  
----------- | ------------------------------------------- | -----------------------------  
Matrix_CSV  | `Matrix_CSV/<MODE>_2020{A,B,C,index_*.csv}` | Assess ▸ Matrix import  
JSON-LD     | `JSON-LD/<MODE>_2020.zip`                  | File ▸ Import ▸ JSON-LD (GUI-friendly)  

Six baseline MSW-management modes (2020 status-quo):  
**JPN · EU · USA · CHN · IND · PMM**  

Each package bundles the product system and all referenced processes & flows (impact-assessment methods **not** included).

---

## 5  Supplementary Data Mapping

Series  | Contents                                      | Repository location  
------- | --------------------------------------------- | --------------------  
**[1]** | Historical / SSP driver data                  | Input for `Skeleton_code/` & `Trained_models/`  
**[2–7]** | Inventories & impacts for six modes           | Source files for `Matrix_CSV/` & `JSON-LD/`  
**[8]** | Scenario impacts 2020–2050                    | Will align with future LCIA updates  
**[9]** | Country-level LCIA results (171 countries)     | Matches model structure  
**[10]** | Grid-coefficient assumptions (Eq. 4)          | Used in RF driver preparation  

Full column descriptions are provided in the paper’s Supplementary-Data guide.

---

## 6  Road-map

- Add 2030–2050 projections & multi-SSP variants for all six modes  
- Release matching **JSON-LD** exports for every dataset  
- Mint DOIs via Zenodo for long-term archiving and citation  

---

## 7  Citing this Repository

```bibtex
@article{Cao2025_NatureSustain,
  author  = {to be supplemented},
  title   = {to be supplemented},
  journal = {Nature Sustainability},
  year    = {2025},
  status  = {to be supplemented}
}

@software{Cao2025_GitHub,
  author = {Qilin Cao},
  title  = {Tailored-Municipal-Solid-Waste-Management-Globally},
  year   = {2025},
  url    = {https://github.com/<your-username>/Tailored-Municipal-Solid-Waste-Management-Globally},
  note   = {Version v1.0, DOI: <to-be-assigned>}
}
```

---

## 8  License

- **Code** — Apache 2.0  
- **Data & models** — Creative Commons Attribution 4.0 International (CC BY 4.0)  

See [`LICENSE`](LICENSE) for full terms.

---

## 9  Contact

- ✉️ <caoql23@mails.jlu.edu.cn> 
- Please open **issues** or **pull requests** for questions, feedback, or contributions.
