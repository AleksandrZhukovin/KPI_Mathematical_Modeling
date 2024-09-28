import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


df = pd.read_csv('saveecobot_17113.csv', usecols=['device_id', 'phenomenon', 'value', 'logged_at'])
df = df.dropna()

# Finding corresponding between different pollution types and display as heatmap
pollutants_list = df["phenomenon"].unique()
r2_matrix = pd.DataFrame(np.zeros((10, 10)), index=pollutants_list, columns=pollutants_list)

model = LinearRegression()
for i, pollutant_x in enumerate(pollutants_list):
    for j, pollutant_y in enumerate(pollutants_list):
        if i != j:
            X = df[df["phenomenon"] == pollutant_x]["value"].values.reshape(-1, 1)[:115000, ]
            y = df[df["phenomenon"] == pollutant_y]["value"].values.reshape(-1, 1)[:115000, ]
            model.fit(X, y)
            r_squared = model.score(X, y)
            r2_matrix.loc[pollutant_x, pollutant_y] = r_squared
plt.figure(figsize=(8, 6))
sns.heatmap(r2_matrix, annot=True, cmap="viridis", cbar=True, linewidths=0.5)
plt.title("Heatmap of R² values between Air Pollutants")
plt.show()

# Get hours from dates as separate column
df["time_of_day"] = df["logged_at"].apply(lambda x:  int(x.split()[1].split(":")[0]))

# Make model of depending no2 pollution from day time
y = df[df["phenomenon"] == 'no2_ug']["value"].values.reshape(-1, 1)
x = df[df["phenomenon"] == 'no2_ug']["time_of_day"].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R^2: {r2}")
print(f"RMSE: {rmse}")


# Make model of depending pm10 pollution from pm1 pollution
x = df[df["phenomenon"] == 'pm10']["value"].values.reshape(-1, 1)[:115000, ]
y = df[df["phenomenon"] == 'pm1']["value"].values.reshape(-1, 1)[:115000, ]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model.fit(x, y)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R^2: {r2}")
print(f"RMSE: {rmse}")
