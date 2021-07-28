import pandas as pd
import matplotlib.pyplot as plt

START_DATE = "2020-08-03"

fig, ax = plt.subplots()
df = pd.read_csv("moisture.csv", header=None, index_col=0, parse_dates=True)
df.columns = ["Value", "Moisture"]
df.loc[START_DATE:]["Moisture"].plot(ax=ax)
fig.show()
