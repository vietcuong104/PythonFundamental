from tabulate import tabulate

data = [["Name", "Place", "Gender"], ["Messi", "Argentina", "Male"], ["Hazel", "America", "Female"], ["Suarez", "Uruguay", "Male"]]
print(tabulate(data))
print("\n")

print(tabulate(data, headers='firstrow'))
print("\n")

print(tabulate(data, headers='firstrow',tablefmt='fancy_grid'))
print("\n")