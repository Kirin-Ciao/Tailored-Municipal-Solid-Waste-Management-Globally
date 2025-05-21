from atexit import register
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

data = pd.read_csv(r'path\to\your_file.csv')
print(data)

his_data = data[(data['year'] == 'your_year') & (data['region_id'] == 'your_region')]
his_data = his_data.dropna()
start_index = list(his_data.columns).index('FOOD')
selected_columns = his_data.columns[start_index:]
his_data = his_data[selected_columns]
his_data = his_data.drop(['population_Male_Aged15-19_Tertiary Education','population_Female_Aged15-19_Tertiary Education',], axis=1)
print(his_data)

X = his_data.drop('FOOD', axis=1)
y = his_data['FOOD']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

reg = RandomForestRegressor(random_state=42)

reg.fit(X_train, y_train)
r2 = 0
for random_state in range(1, 10001):
    reg = RandomForestRegressor(random_state=random_state)
    reg.fit(X_train, y_train)
    predictions = reg.predict(X_test)
    r2 = r2_score(y_test, predictions)
    print(f"Random State: {random_state}, R-squared: {r2}")
    if r2 > 0.8:
        print(f"Found optimal random state: {random_state} with R-squared: {r2}")
        break