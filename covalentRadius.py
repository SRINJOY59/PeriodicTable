import periodictable
import matplotlib.pyplot as plt

x = []
y = []

for element in periodictable.elements:
    y.append(element.number)
    x.append(element.covalent_radius) 

plt.plot(x, y)
plt.ylabel("Element Number")
plt.xlabel("Element's covalent Radius")
plt.show()