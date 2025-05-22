Random-Forest (MSW Forecasting)

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
