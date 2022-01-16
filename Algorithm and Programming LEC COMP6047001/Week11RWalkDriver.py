#%%
import matplotlib.pyplot as plt
from myRWalk import RandomWalk

rw = RandomWalk()
rw.fillWalk()

plt.scatter(rw.xValues,rw.yValues,s=3)
#plt.plot(rw.xValues,rw.yValues,linewidth=3)
plt.show()
#%%
