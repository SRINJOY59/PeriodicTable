import periodictable

atomic_no = int(input("Enter the atomic number: "))
element = periodictable.elements[atomic_no]

isotopes = element.isotopes

# Print the name and mass of each isotope
for isotope in isotopes:
    print(f"{isotope.name}: {isotope.mass}")

