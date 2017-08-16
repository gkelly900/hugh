import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from matplotlib import rc

rc('font', **{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
matplotlib.style.use('ggplot')

df = pd.read_csv("hugh_data.csv")

df["MovingAverage"] = df.Vint_Temp.rolling(10).mean()

df["TemperatureDifference"] = df.Vint_Temp - df.MovingAverage


df['Surrond']=np.nan

for i in range(0,4):
    df['Surrond'][(df.Sulphate>0).shift(i).fillna(False)]=df['Year']-i


df['Before']=np.nan

for i in range(-4,0):
    df['Before'][(df.Sulphate>0).shift(i).fillna(False)]=df['Year']-i


df["All"] = np.nan

for i in range(-4,4):
    df['All'][(df.Sulphate>0).shift(i).fillna(False)]=df['Year']-i



difference = []
sulphate = []

years = df.Surrond.unique()
i = 1
for year in years:
    if i == 1:
        i +=1
        continue
    mean_before = df.Vint_Temp[(df["Before"] == year) & (df["All"] == year)].mean()
    min_after = df.Vint_Temp[df["Surrond"] == year].min()
    diff = min_after - mean_before
    sulph = df.Sulphate[df["Surrond"] == year].max()

    difference.append(diff)
    sulphate.append(sulph)


plt.scatter(sulphate, difference)
plt.show()
