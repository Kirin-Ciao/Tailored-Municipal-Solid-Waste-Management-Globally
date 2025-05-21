from atexit import register
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv(r'path\to\your_file.csv')
print(data)

pre_data = data[(data['year'] == 'pre_year')]
start_index = list(pre_data.columns).index('REGION')
selected_columns = pre_data.columns[start_index:]
pre_data = pre_data[selected_columns]
pre_data = pre_data.drop(['region_id','total_msw_ton', 'country_name', 'population_Male_Aged15-19_Tertiary Education','population_Female_Aged15-19_Tertiary Education'], axis=1)
print(pre_data)

with open('path\to\Trained_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    
X_SSP1 = pre_data
X_SSP1 = X_SSP1.set_index('REGION')
X_SSP1 = X_SSP1.dropna()

SSP1_predictions = loaded_model.predict(X_SSP1)

predictions_df = pd.DataFrame({
    'REGION': X_SSP1.index, 
    '2030': SSP1_predictions 
})

predictions_df.to_csv('path\to\your_file.csv', index=False)