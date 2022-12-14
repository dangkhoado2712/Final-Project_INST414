
# Regression analysis
# dependent: people fully vaccinated
# Independent: Totlal vaccination, daily vaccination, total distributed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

df = pd.read_csv("G:\My Drive\Fall2022\INST414\Final Project\cleaned_states.csv")
df
df.drop("Unnamed: 0",axis=1, inplace=True)


# Regression analysis for the Maryland area

# Extarct the data for MD  
df_MD = df[df['location'] == 'Maryland']
df_MD
df_MD.dropna(inplace = True)
df_MD.columns

# Extarct the data for VA  
df_VA = df[df['location'] == 'Virginia']
df_VA
df_VA.dropna(inplace = True)
df_VA.columns


# Get to know the data
df_MD['location'].value_counts()

#Regression analysis

y = df_MD['people_fully_vaccinated']
x1 = df_MD['total_vaccinations']
x2 = df_MD['daily_vaccinations']
x3 = df_MD ['total_distributed']

# Linear Regression model

#Model 1: people fully vaccinated as a function of total vaccinations
plt.ylabel("People fully vaccinated")
plt.xlabel("Total vaccinations")
plt.scatter(x1, y)

x1 = np.array (x1).reshape (-1, 1)
print(x1)
print (x1.shape)
print (y.shape)
model1 = LinearRegression()
model1.fit(x1, y)
model1.intercept_
model1.coef_
r_sq = model1.score(x1,y)
print(r_sq)

y_pred = model1.predict(x1)
plt.ylabel("People fully vaccinated")
plt.xlabel("Total vaccinations")
plt.scatter(x1,y)
plt.plot (x1,y_pred)

#Model 2: people fully vaccinated as a function of daily vaccinations
plt.ylabel("People fully vaccinated")
plt.xlabel("daily vaccinations")
plt.scatter(x2, y)

x2 = np.array (x2).reshape (-1, 1)
print(x2)
print (x2.shape)
print (y.shape)
model1 = LinearRegression()
model1.fit(x2, y)
model1.intercept_
model1.coef_
r_sq = model1.score(x2,y)
print(r_sq)

y_pred = model1.predict(x2)
plt.ylabel("People fully vaccinated")
plt.xlabel("daily vaccinations")
plt.scatter(x2,y)
plt.plot (x2,y_pred)

#Model 3: people fully vaccinated as a function of  total distributed
plt.ylabel("People fully vaccinated")
plt.xlabel("Total vaccinations")
plt.scatter(x3, y)

x3 = np.array (x3).reshape (-1, 1)
print(x3)
print (x3.shape)
print (y.shape)
model1 = LinearRegression()
model1.fit(x3, y)
model1.intercept_
model1.coef_
r_sq = model1.score(x3,y)
print(r_sq)

y_pred = model1.predict(x3)
plt.ylabel("People fully vaccinated")
plt.xlabel("Total vaccinations")
plt.scatter(x3,y)
plt.plot (x3,y_pred)

# Model 12: people fully vaccinated as a function of total vaccinations adn daily vaccinations
x2 = np.array (x2).reshape (-1, 1)

x12 = np.concatenate ((x1, x2), axis = 1)
print (x12)
print (x12.shape)
model12 = LinearRegression()
model12.fit(x12,y)
model12.intercept_
model12.coef_
r_sq = model12.score(x12,y)
print (r_sq)

# Model 123: people fully vaccinated as a function of total vaccinations adn daily vaccinations,
# total distributed
x3 = np.array (x3).reshape (-1, 1)
x123 = np.concatenate ((x1, x2, x3), axis = 1)
print (x123)
print (x123.shape)
model123 = LinearRegression()
model123.fit(x123,y)
model123.intercept_
model123.coef_
r_sq = model123.score(x123,y)
print (r_sq)

