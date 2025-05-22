# Tailored-Municipal-Solid-Waste-Management-Globally
Reproducible RF-based MSW forecasting & openLCA system models for our Nature Sustainability study on globally tailored waste management.
---

## Table of Contents
1. [Repository Overview](#repository-overview)
2. [Random-Forest (MSW Forecasting)](#random-forest-msw-forecasting)
3. [LCIA Product-System Models](#lcia-product-system-models)
4. [Supplementary Data Mapping](#supplementary-data-mapping)
5. [Road-map](#road-map)
6. [Citing this Repository](#citing-this-repository)
7. [License](#license)
8. [Contact](#contact)

---

## 1 Repository Overview
| Branch | Key folders / files | Purpose |
|--------|---------------------|---------|
| `main` | `README`, `CITATION.cff`, issue tracker | Entry point |
| `RandomForest-Forecasting` | `Skeleton_code/`, `Trained_models/`, `PRE_code.py`, `Pipeline1.py`, `Pipeline2.py` | 🔮 MSW generation & composition projection |
| `LCIA-models-openLCA` | `Matrix_CSV/` (raw **A/B/C** matrices) <br> `JSON-LD/` (`*.zip` archives) | ♻️ Life-cycle inventory & impact models |

---

## 2  Random-Forest (MSW Forecasting)

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

## 3  LCIA Product-System Models

Format      | Location                                    | How to use in openLCA 2.0.4  
----------- | ------------------------------------------- | -----------------------------  
Matrix_CSV  | `Matrix_CSV/<MODE>_2020{A,B,C,index_*.csv}` | Assess ▸ Matrix import  
JSON-LD     | `JSON-LD/<MODE>_2020.zip`                  | File ▸ Import ▸ JSON-LD (GUI-friendly)  

Six baseline MSW-management modes (2020 status-quo):  
**JPN · EU · USA · CHN · IND · PMM**  

Each package bundles the product system and all referenced processes & flows (impact-assessment methods **not** included).

---

## 4  Supplementary Data Mapping

Series  | Contents                                      | Repository location  
------- | --------------------------------------------- | --------------------  
**[1]** | Historical / SSP driver data                  | Input for `Skeleton_code/` & `Trained_models/`  
**[2–7]** | Inventories & impacts for six modes           | Source files for `Matrix_CSV/` & `JSON-LD/`  
**[8]** | Scenario impacts 2020–2050                    | Will align with future LCIA updates  
**[9]** | Country-level LCIA results (171 countries)     | Matches model structure  
**[10]** | Grid-coefficient assumptions (Eq. 4)          | Used in RF driver preparation  

Full column descriptions are provided in the paper’s Supplementary-Data guide.

---

## 5  Road-map

- Add 2030–2050 projections & multi-SSP variants for all six modes  
- Release matching **JSON-LD** exports for every dataset  
- Mint DOIs via Zenodo for long-term archiving and citation  

---

## 6  Citing this Repository

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
