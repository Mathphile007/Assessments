

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df=pd.read_csv("/content/booking.csv")

df.head(10)

df.shape

df.duplicated().sum() #there is no duplicates

df.nunique()

df.drop(["Booking_ID"],axis=1) #ID column wont be helpful so removing it

df["date of reservation"]

pd.to_datetime(df["date of reservation"],format='mixed')

#1 Handling missing and outliers
df.isnull().sum()

sns.distplot(df['average price'])

df['average price'] = df['average price'].fillna(df['average price'].mean())

df['room type']

df['room type'].fillna('Room_Type 1')

sns.histplot(df['room type'])
#Lets fill Room type-1 -mode

df.isnull().sum()

numerical_columns=df.select_dtypes(include=['int']).columns.tolist()

#Outlier handling
def detect_outliers_iqr(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (data < lower_bound) | (data > upper_bound)

outliers = detect_outliers_iqr(df[numerical_columns])
df_outliers_removed = df[~outliers.any(axis=1)]

df_outliers_removed.drop('date of reservation',axis=1)

#2
categorical_cols = df_outliers_removed.select_dtypes(include=['object']).columns.tolist()
df_encoded = pd.get_dummies(df_outliers_removed, columns=categorical_cols)
df_encoded = df_encoded.astype(int)

#3 Feature selection from correlation
df_encoded.corr()
# Create correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df_encoded.corr(), annot=True)
plt.title('Correlation')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler

#4
numeric_cols = df_encoded.select_dtypes(include=['int']).columns.tolist()
scaler = MinMaxScaler()
df_encoded[numeric_cols] = scaler.fit_transform(df_encoded[numeric_cols])
df_encoded.head()


X = df_encoded.drop('booking status', axis=1)
y = df_encoded['booking status']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#5
logistic_model = LogisticRegression(max_iter=1000)

logistic_model.fit(X_train, y_train)

y_pred = logistic_model.predict(X_test)

#6
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_report_str = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{classification_report_str}")

conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()