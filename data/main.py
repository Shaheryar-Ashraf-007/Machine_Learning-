import numpy
import matplotlib.pyplot as plt

speed = [99,86,88,111,101,87,110,90,80,85,95]
x = numpy.mean(speed)
print(x)
plt.plot(speed)


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints,marker='o')
plt.show()


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()
plt.show()


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

