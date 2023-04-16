import periodictable
import matplotlib.pyplot as plt

x = []
y = []

for element in periodictable.elements:
    y.append(element.number)
    x.append(element.mass) 

plt.scatter(x, y)
plt.ylabel("Element Number")
plt.xlabel("Element Masses")
plt.show()