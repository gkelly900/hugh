import pandas as pd
import numpy as np
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

df = pd.read_csv("hugh_data.csv")

df["MovingAverage"] = df.Vint_Temp.rolling(2).mean()

dfs = np.array_split(df,7)

df.describe()

df854 = df[(df["Year"] < 870) & (df["Year"] > 830)]

df854.apply()



ax = df854.plot(x='Year', y=['Vint_Temp','MovingAverage'],
        figsize=(20,10), style=['r-', 'g-'])

ax.set_ylabel('Temperature Fluctuations (K)')
plt.axvline(x=854, color="b")
plt.xlabel('Year', fontsize=16)
plt.title("Temperature Fluctuations (Buntgen et al 2011) and Sulphate Emissions (Gao et al 2008) by Year")
plt.show()
#plt.savefig("bunt_temp{}.jpg".format(i))


for i in range(0,7):
    ax = dfs[i].plot(x='Year', y=['Bunt_Temp','Sulphate'], secondary_y=['Sulphate'],
            figsize=(20,10), style=['r-', 'b+'])

    ax.set_ylabel('Temperature Fluctuations (K)')
    ax.right_ax.set_ylabel('Sulphate Emission (Tg)')
    plt.xlabel('Year', fontsize=16)
    plt.title("Temperature Fluctuations (Buntgen et al 2011) and Sulphate Emissions (Gao et al 2008) by Year")
    plt.savefig("bunt_temp{}.jpg".format(i))

for i in range(0,7):
    ax = dfs[i].plot(x='Year', y=['Bunt_Precip','Sulphate'], secondary_y=['Sulphate'],
            figsize=(20,10), style=['r-', 'b+'])

    ax.set_ylabel('Precipitation')
    ax.right_ax.set_ylabel('Sulphate Emission (Tg)')
    plt.xlabel('Year', fontsize=16)
    plt.title("Precipitation (Buntgen et al 2011) and Sulphate Emissions (Gao et al 2008) by Year")
    plt.savefig("bunt_precip{}.jpg".format(i))
    #plt.show()
