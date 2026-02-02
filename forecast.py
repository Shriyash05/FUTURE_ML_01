import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

df = pd.read_csv("train.csv", parse_dates=["date"])
df = df.sort_values("date")

df = df.groupby("date")["sales"].sum()
df = df.asfreq("D").ffill()

train = df[:-90]
test = df[-90:]

model = ExponentialSmoothing(
    train,
    trend="add",
    seasonal="add",
    seasonal_periods=7
)

fit = model.fit()
forecast = fit.forecast(90)

print("MSE:", round(mean_squared_error(test, forecast), 2))
print("MAPE:", round(mean_absolute_percentage_error(test, forecast), 4))

plt.figure(figsize=(12,6))
plt.plot(train.index, train, label="Historical Sales")
plt.plot(test.index, test, label="Actual Sales")
plt.plot(forecast.index, forecast, label="Forecasted Sales")
plt.legend()
plt.title("Sales & Demand Forecast")
plt.savefig("sales_forecast.png")
plt.close()

pd.DataFrame({
    "date": forecast.index,
    "forecasted_sales": forecast.values
}).to_csv("forecasted_sales.csv", index=False)