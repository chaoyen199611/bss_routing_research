from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("result.csv")
df.drop(columns=["Unnamed: 0"],inplace = True)
df = df[df.capacity != 0]
df = df.to_numpy().astype(int)

print(df)

smin_bound = df[:,0]
smax_bound = df[:,1]
capacity = df[:,3]
start = df[:,4]



plt.show()

fig,a = plt.subplots()
for i in range (len(capacity)):

    x = np.array([i+1, i+1, i+1, i+1])
    y = np.array([capacity[i], smax_bound[i], smin_bound[i],0])
    if start[i]<=smin_bound[i] or start[i]>=smax_bound[i]:
        plt.plot(i+1,start[i], marker='^', ls='none',mec='black',mfc='black',ms=3)
    else:
        plt.plot(i+1,start[i], marker='.', ls='none',mec='black',mfc='black')

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:3], points[-3:]], axis=1)
    line_styles = [("dotted"),("solid")]
    lc = LineCollection(segments, linestyles=line_styles, color='black')
    a.add_collection(lc)



a.set_xlim(0,52)
a.set_ylim(0,50)

a.set_xlabel('statoin')
a.set_ylabel('bikes')
a.set_ylim(0, 50)
a.set_title('stations service_level at 2023 April first to fifth, 6 a.m. - 9 a.m.')

plt.show()
    