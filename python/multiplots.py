import matplotlib.pyplot as plt

plt.subplot(1, 3, 1) #1 row, 3 columns, working on 1st plot
x=range(0,10,1)
plt.plot(x, "r")

plt.subplot(1,3,2)
y=range(10,0,-1)
plt.plot(y, "b")

plt.subplot(1,3,3)
z=[4]*10
plt.plot(z, "g")

plt.show()
