import periodictable
import matplotlib.pyplot as plt

atomicNo = int(input("Enter the atomic number of the element: "))
element = periodictable.elements[atomicNo]
print("Atomic Number: ", element.number)
print("Symbol: ", element.symbol)
print("Name: ", element.name)
print("Atomic Mass: ", element.mass)
print("Density: ", element.density)