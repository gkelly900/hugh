import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from matplotlib import rc

rc('font', **{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
matplotlib.style.use('ggplot')

df = pd.read_csv("hugh_data.csv")

df.describe()

df['Surrond']=np.nan

for i in range(0,4):
    df['Surrond'][(df.Sulphate>0).shift(i).fillna(False)]=df['Year']-i


df['Before']=np.nan

for i in range(-15,0):
    df['Before'][(df.Sulphate>0).shift(i).fillna(False)]=df['Year']-i


df["All"] = np.nan

for i in range(-15,4):
    df['All'][(df.Sulphate>0).shift(i).fillna(False)]=df['Year']-i


kob_temp_stats_list = []
vint_temp_stats_list = []
bunt_temp_stats_list = []

years = df.Surrond.unique()
i = 1
for year in years:
    if i == 1:
        i +=1
        continue
    mean_before = df.Kob_Temp[(df["Before"] == year) & (df["All"] == year)].mean()
    std_before = df.Kob_Temp[(df["Before"] == year) & (df["All"] == year)].std()
    min_after = df.Kob_Temp[df["Surrond"] == year].min()

    significance = (mean_before - min_after)/std_before

    sulphate = df.Sulphate[df["Surrond"] == year].max()

    kob_temp_stats_list.append([year, sulphate, mean_before, std_before, min_after, significance])

    mean_before = df.Vint_Temp[(df["Before"] == year) & (df["All"] == year)].mean()
    std_before = df.Vint_Temp[(df["Before"] == year) & (df["All"] == year)].std()
    min_after = df.Vint_Temp[df["Surrond"] == year].min()
    mean_after = df.Vint_Temp[df["Surrond"] == year].mean()
    significance = (mean_before - min_after)/std_before

    vint_temp_stats_list.append([year, sulphate, mean_before, std_before, mean_after, min_after, significance])

    mean_before = df.Bunt_Temp[(df["Before"] == year) & (df["All"] == year)].mean()
    std_before = df.Bunt_Temp[(df["Before"] == year) & (df["All"] == year)].std()
    min_after = df.Bunt_Temp[df["Surrond"] == year].min()

    significance = (mean_before - min_after)/std_before

    bunt_temp_stats_list.append([year, sulphate, mean_before, std_before, min_after, significance])

vint_temp_stats_list

df_vint = pd.DataFrame(vint_temp_stats_list, columns = ["EruptionYear",
                                                        "SulphateTg",
                                                        "MeanBefore",
                                                        "StDevBefore",
                                                        "MeanAfter",
                                                        "MinAfter",
                                                        "Significance"])





df_vint

data = np.array(vint_temp_stats_list)

plt.scatter(data[:,5], data[:,1])
plt.xlabel('Statistical Significance ($\sigma)')
plt.ylabel("Sulphate Emission (Tg)")
plt.xlim([-3,5])
plt.show()

df[(df["All"] == 898)]


df.Before[df["Before"] == 1991.]

means = df.groupby('Before').mean()
means.Bunt_Temp

df.describe()
df[df["Surrond"] == 0]

df.groupby(by="Surrond")

df.Surrond.unique()

data = df.as_matrix()

df

data
i = 1
for v in df.Surrond.unique():
    if i == 1:
        i += 1
        continue
    else:
        print(max(df.loc[df['Surrond'] == v, 'DecreaseTempBunt']))
        i += 1
