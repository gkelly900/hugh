import pandas as pd
import numpy as np
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
rc('text', usetex=False)

df = pd.read_csv("hugh_data.csv")

df["MovingAverage"] = df.Vint_Temp.rolling(2).mean()

dfs = np.array_split(df,7)

df.describe()

df854 = df[(df["Year"] < 870) & (df["Year"] > 830)]


ax = df854.plot(x='Year', y=['Vint_Temp','MovingAverage'],
        figsize=(20,10), style=['r-', 'g-'])

ax.set_ylabel('Temperature Fluctuations (K)')
plt.axvline(x=854, color="b")
plt.xlabel('Year', fontsize=16)
plt.title("Temperature Fluctuations (Buntgen et al 2011) and Sulphate Emissions (Gao et al 2008) by Year")
plt.show()
#plt.savefig("bunt_temp{}.jpg".format(i))


for i in range(0,7):
    ax = dfs[i].plot(x='Year', y=['Vint_Temp','Sulphate'], secondary_y=['Sulphate'],
            figsize=(20,10), style=['r-', 'b+'])

    ax.set_ylabel('Temperature Fluctuations (K)')
    ax.right_ax.set_ylabel('Sulphate Emission (Tg)')
    plt.xlabel('Year', fontsize=16)
    plt.title("Temperature Fluctuations (Vinther et al 2010) and Sulphate Emissions (Gao et al 2008) by Year")
    plt.savefig("vint_temp{}.jpg".format(i))

for i in range(0,7):
    ax = dfs[i].plot(x='Year', y=['Wilson_Precip','Sulphate'], secondary_y=['Sulphate'],
            figsize=(20,10), style=['r-', 'b+'])

    ax.set_ylabel('Precipitation')
    ax.right_ax.set_ylabel('Sulphate Emission (Tg)')
    plt.xlabel('Year', fontsize=16)
    plt.title("Precipitation (Wilson et al 2013) and Sulphate Emissions (Gao et al 2008) by Year")
    plt.savefig("wils_precip{}.jpg".format(i))
    #plt.show()
