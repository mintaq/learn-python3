from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon"]
table.add_row(["Pikachu"])
table.add_row(["Raichu"])
table.add_row(["Chamender"])
table.align = "l"
print(table)