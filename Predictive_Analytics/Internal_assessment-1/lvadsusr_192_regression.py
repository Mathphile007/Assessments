

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import confusion_matrix

df=pd.read_csv("/content/expenses.csv")

df.head(10)

print('Shape of the data: ', df.shape)

df.dtypes

df.describe()

df.info()

df.columns = df.columns.str.strip()

df.nunique()

#1 Handling missing values
print('Total missing values in the data: ', df.isnull().sum().sum(), '\n\n')
print('Missing values per column \n\n',df.isnull().sum())

sns.distplot(df['bmi'])
#As the bmi column is normally distrubuted we can fill the missing values by mean

df['bmi'] = df['bmi'].fillna(df['bmi'].mean())

print('Missing values per column after filling  \n\n',df.isnull().sum())

sns.boxplot(df)

#Outlier handling
def detect_outliers_iqr(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (data < lower_bound) | (data > upper_bound)

outliers = detect_outliers_iqr(df[['age','bmi','children','charges']])
df_outliers_removed = df[~outliers.any(axis=1)]

df_outliers_removed.shape

df.shape

#2 Encoding Categorical Data
categorical_cols = df_outliers_removed.select_dtypes(include=['object']).columns.tolist()
df_encoded = pd.get_dummies(df_outliers_removed, columns=categorical_cols)

#3 Feature Selection and Data Cleaning
df_encoded.corr()
# Create correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df_encoded.corr(), annot=True)
plt.title('Correlation')
plt.show()

#All columns given in the data seems to be relevant for prediction as they have
#good correlation with the target column-Charges

df_encoded.duplicated().sum()

df_encoded.drop_duplicates(inplace=True)

df_encoded.astype(int)

#4 Data Splitting
X=df_encoded.drop(['charges'],axis=1)
X

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

y=df_encoded['charges']

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

#5
LR = LinearRegression()
LR.fit(X_train, y_train)

#6 Model Evaluation

# Train data

print('Coefficient of determination: ', LR.score(X_train, y_train))
y_pred = LR.predict(X_train)
print('R^2: ', r2_score(y_train, y_pred))
print('MAE: ',mean_absolute_error(y_train, y_pred))
print('MSE: ', mean_squared_error(y_train, y_pred))
print('RMSE: ', np.sqrt(mean_squared_error(y_train, y_pred)))

# Test data
print('Coefficient of determination: ', LR.score(X_test, y_test))
y_pred_test = LR.predict(X_test)
print('R^2: ', r2_score(y_test, y_pred_test))
print('MAE: ',mean_absolute_error(y_test, y_pred_test))
print('MSE: ', mean_squared_error(y_test, y_pred_test))
print('RMSE: ', np.sqrt(mean_squared_error(y_test, y_pred_test)))

#Insights
The key factors driving insurance costs is the person's choice of smoking being yes as it positively correlated with the charges
and also age of the person is also positively correlated

