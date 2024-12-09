import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

data = {
    "Year": [
        2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2022
    ],
    "Value": [
        1730988, 1648910, 1753543, 
        1786554, 1972328, 2111839, 2167361, 1979283, 2087076, 2178848, 2246206, 
        2342451, 2523975, 2673621.24, 2705312, 2583448, 2489091, 2492676, 2569572
    ]
}

df = pd.DataFrame(data)

X = np.array(df["Year"]).reshape(-1, 1)
y = np.array(df["Value"])

model = LinearRegression()
model.fit(X, y)

# Predict 
year_2023 = np.array([[2023]])
prediction_2023 = model.predict(year_2023)[0]

# Plot
plt.figure(figsize=(10, 6))

plt.scatter(df["Year"], df["Value"], color='blue', label='Actual Data')
plt.plot(df["Year"], model.predict(X), color='red', label='Regression Line')
plt.scatter(2023, prediction_2023, color='green', label='2023 Prediction')

plt.title("Linear Regression to Predict 2023 Immigrant Population", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Immigration Population", fontsize=14)
plt.grid(alpha=0.5)
plt.legend(fontsize=12)
plt.savefig("immigrate_LR.pdf", format="pdf", bbox_inches="tight")
plt.show()