import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import linregress
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


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
wils_precip_stats_list = []

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
    difference = mean_before - min_after

    vint_temp_stats_list.append([year, sulphate, mean_before, std_before, mean_after, min_after, difference])

    mean_before = df.Bunt_Temp[(df["Before"] == year) & (df["All"] == year)].mean()
    std_before = df.Bunt_Temp[(df["Before"] == year) & (df["All"] == year)].std()
    min_after = df.Bunt_Temp[df["Surrond"] == year].min()

    significance = (mean_before - min_after)/std_before

    bunt_temp_stats_list.append([year, sulphate, mean_before, std_before, min_after, significance])

    mean_before = df.Wilson_Precip[(df["Before"] == year) & (df["All"] == year)].mean()
    std_before = df.Wilson_Precip[(df["Before"] == year) & (df["All"] == year)].std()
    min_after = df.Wilson_Precip[df["Surrond"] == year].min()
    mean_after = df.Wilson_Precip[df["Surrond"] == year].mean()
    significance = (mean_before - mean_after)/std_before

    wils_precip_stats_list.append([year, sulphate, mean_before, std_before, mean_after, significance])

df_vint = pd.DataFrame(vint_temp_stats_list, columns = ["EruptionYear",
                                                        "SulphateTg",
                                                        "MeanBefore",
                                                        "StDevBefore",
                                                        "MeanAfter",
                                                        "MinAfter",
                                                        "Difference"])


x = df_vint.SulphateTg.values
y = df_vint.Difference.values
mask = ~np.isnan(x) & ~np.isnan(y)
x = x[mask].reshape(55, 1)
y = y[mask].reshape(55, 1)

regr = linear_model.LinearRegression()
regr.fit(x,y)

y_pred = regr.predict(x)
regr.intercept_[0]

print('Coefficients: \n', regr.coef_[0][0])

print("Mean squared error: %.2f"
      % mean_squared_error(y, y_pred))

print('Variance score: %.2f' % r2_score(y,y_pred))

plt.figure(figsize=(12,8))
plt.scatter(x, y,  color='black')
plt.plot(x, regr.predict(x), color='blue', linewidth=1)
plt.xlabel("Sulphate Emission (Tg)")
plt.ylabel("Temperature Difference (K)")
plt.title("Linear Regression of Temperature Difference (Vinther) by Sulphate Emission (Gao)")
plt.axhline(0, color='white', linewidth=4)
plt.annotate('TempDiff = {0:.3f}*Suphate + {1:.2f}'.format(regr.coef_[0][0],
                                                 regr.intercept_[0]),
             xy=(100, 3), fontsize=14
            )
plt.annotate('R**2 Score: {0:.2f}'.format(r2_score(y,y_pred)),
             xy=(100, 2.5), fontsize=14
            )
plt.savefig("linear_regression_vint_temp.jpg")

df_wils = pd.DataFrame(wils_precip_stats_list, columns = ["EruptionYear",
                                                        "SulphateTg",
                                                        "MeanBefore",
                                                        "StDevBefore",
                                                        "MeanAfter",
                                                        "Significance"])

df_wils

yw = df_wils.SulphateTg.values
xw = df_wils.Significance.values

plt.figure(figsize=(12,8))
plt.scatter(xw, yw,  color='green')
plt.ylabel("Sulphate Emission (Tg)")
plt.xlabel("Statistical Significance (Standard Deviations)")
plt.title("Statisitcal Signifcance of Precipitation Changes (Wilson) by Sulphate Emission (Gao)")
plt.savefig("Wils_Precip_sigbymean.jpg")

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
