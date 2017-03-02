import matplotlib.pyplot as plt

Time=[0,1,2,3,4,5,6]
CO2=[250, 265, 272, 260, 300, 320, 389]
Temp=[14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

fig, ax1=plt.subplots()

ax1.plot(Time, CO2, "r*-")
ax1.set_ylabel("[CO2]")

ax2=ax1.twinx()

ax2.plot(Time, Temp, "b--")
ax2.set_ylabel("Temp (degC)")

plt.show()
