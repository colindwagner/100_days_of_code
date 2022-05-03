# search for packages on pypi


from prettytable import PrettyTable



table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"

#, "Pikachu", "Squirtle", "Charmander"
print(table)


