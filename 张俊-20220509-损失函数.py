from sklearn.metrics import mean_squared_error, r2_score

import numpy as np

print(f"均方误差(MSE)：{mean_squared_error(result, test_y)}")  #均值
print(f"根均方误差(RMSE)：{np.sqrt(mean_squared_error(result, test_y))}")
print(f"测试集R^2：{r2_score(test_y, result)}")