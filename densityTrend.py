import periodictable
import matplotlib.pyplot as plt

x = []
y = []
for element in periodictable.elements:
    y.append(element.number)
    x.append(element.density)

plt.scatter(x, y)
plt.ylabel("Element Atomic Number")
plt.xlabel("Element Density")
plt.show()
