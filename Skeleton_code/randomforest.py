from atexit import register
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import mean_squared_error
import numpy as np

# 读取CSV文件
data = pd.read_csv(r'path\to\your_file.csv')
print(data)

# 提取历史数据
his_data = data[(data['year'] == 'your_year') & (data['region_id'] == 'your_region')]
## 数据清洗，比如：剔除含有NaN项的数据
his_data = his_data.dropna()
# 切片某种MSW成份，比如：'FOOD'
start_index = list(his_data.columns).index('FOOD')
selected_columns = his_data.columns[start_index:]
his_data = his_data[selected_columns]
print(his_data)

# 拆分数据集
X = his_data.drop('FOOD', axis=1)
y = his_data['FOOD']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建随机森林回归器
reg = RandomForestRegressor(random_state=42)

# 设置超参数候选值
param_grid = {
    'n_estimators': [300, 350, 400], 
    'max_features': [30, 35, 38], 
    'min_samples_leaf': [1, 2, 3] 
}

# 使用GridSearchCV进行超参数搜索，并获取最佳组合
grid_search = GridSearchCV(estimator=reg, param_grid=param_grid, scoring='neg_mean_squared_error', cv=3)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
print("Best Parameters:", best_params)

# 创建最佳参数下的随机森林回归器
best_reg = RandomForestRegressor(n_estimators=best_params['n_estimators'],
max_features=best_params['max_features'],
min_samples_leaf=best_params['min_samples_leaf'],
random_state=42)

# 训练随机森林模型
best_reg.fit(X_train, y_train)
importances = best_reg.feature_importances_
print(importances) ##各特征变量的重要程度，值越大，特征越重要
feature_importances = pd.DataFrame({
    'Feature': X.columns,  
    'Importance': best_reg.feature_importances_  # 特征的重要性
})

# 保存特征重要性
feature_importances.to_csv(r'path\to\feature_importances_FOOD.csv', index=False)

# 预测测试集
predictions = best_reg.predict(X_test)

# 计算R2
r2 = r2_score(y_test, predictions)
print("R-squared:", r2)
# 计算均方误差
mse = mean_squared_error(y_test, predictions)
# 计算均方根误差
rmse = np.sqrt(mse)
print("Root Mean Squared Error (RMSE):", rmse)


# 提取要预测的数据
data_pre = data[(data['year'] == 'your_year') & (data['region_id'] == 'your_region')]
data_pre = data_pre.dropna()
start_index = list(data_pre.columns).index('FOOD')
selected_columns = data_pre.columns[start_index:]
data_pre = data_pre[selected_columns]
print(data_pre)

X_new = data_pre.drop('FOOD', axis=1)
y_new = data_pre['FOOD']

predicted_MSW = best_reg.predict(X_new)
print("Predicted MSW:", predicted_MSW)

# 绘图
plt.figure(figsize=(10, 6))
plt.scatter(y_new, predicted_MSW, color='blue', label='Predicted')
plt.plot([min(y_new), max(y_new)], [min(y_new), max(y_new)], linestyle='--', color='red', label='Perfect Prediction')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.legend()
plt.show()

# 保存模型
with open('path\to\FOOD_model.pkl', 'wb') as f:
    pickle.dump(best_reg, f)