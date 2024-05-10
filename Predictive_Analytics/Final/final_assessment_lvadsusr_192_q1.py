# -*- coding: utf-8 -*-
"""Final_Assessment_LVADSUSR_192_Q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bENd8jp003Mi-YEq3fypZi0dJ4eo26zo
"""

#Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import confusion_matrix

df=pd.read_csv("/content/Fare prediction.csv")

df.head(10)

df.info()

#Converting into datetime and extracting the useful information time of ride to understand the peak hours and inculcate the traffic conditions history
#assumption is 24-is considered as midnight 12
df['pickup_datetime']=pd.to_datetime(df['pickup_datetime'])

df["time_of_ride"]=df['pickup_datetime'].dt.time.astype(str)

df['time_of_ride']

df["time"]=df["time_of_ride"].str[:2]

df['time']=df['time'].astype(int).replace(0,24)

print('Shape of the data: ', df.shape)

df.info()

numeric_cols = df.select_dtypes(include=['int','float']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
print(numeric_cols)
print(categorical_cols)

#Removing the categorical columns  as we dont need it for model
df.drop(categorical_cols,axis=1,inplace=True)



#1 Handling missing values
print('Total missing values in the data: ', df.isnull().sum().sum(), '\n\n')
print('Missing values per column \n\n',df.isnull().sum())

#EDA
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()

#Box plot
for column in numerical_columns:
  sns.boxplot(df[column])
  plt.show()

for column in df.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 5))
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Bar Chart of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix:\n", correlation_matrix)

import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

sns.boxplot(df)
#Outlier handling
def detect_outliers_iqr(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (data < lower_bound) | (data > upper_bound)

outliers = detect_outliers_iqr(df[numeric_cols])

df_outliers_removed = df[~outliers['fare_amount']==True]
print(df_outliers_removed.shape)
print(df.shape)
#Fare amount column-outliers treated

#Adding extra feature



# Create correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df_outliers_removed[numeric_cols].corr(), annot=True)
plt.title('Correlation')
plt.show()

#All numeric columns given in the data seems to be relevant for prediction as they have
#good correlation with the target column-fare amount

df_outliers_removed.duplicated().sum()
#No duplicates

#Data Splitting
X=df_outliers_removed.drop(['fare_amount','pickup_datetime'],axis=1)
X

#Scaling data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)

final_df=df_outliers_removed.drop('pickup_datetime',axis=1)

y=final_df['fare_amount']

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

#Model building
LR = LinearRegression()
LR.fit(X_train, y_train)

#Model Evaluation
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

#There is good correlation between time and fare price so adding feature whether peak or not can enhance the prediction



