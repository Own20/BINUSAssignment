import matplotlib.pyplot as plt
from Week11MyRandomWalk import RandomWalk

rw = RandomWalk()
rw.fillWalk()
plt.scatter(rw.xValues, rw.yValues, s=15)
plt.show()

plt.scatter(rw.xValues, rw.yValues, s=3)
plt.plot(rw.xValues, rw.yValues, linewidth=3)
plt.show()