
#prettytable1
#7.10.25
#N mazzetti

list1 = [ "Dembele", "Lamine", "vitinha", "salah", "raphina" , "hakimi", "mabppe", "Palmer", "Donnarumma" , "Mendes"]
list2 = [ "90€ Million", "200€ Million","80€ Million", "50€ Million", "90€ Million", "80€ Millipn", "180€ Million" , "120€ Million", "40€ Million", "70€ Million"]

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = [" Top 10 footballers in the world ", "Market value"]

'''for name in list1:
    table.add_row([name])
'''
for index in range(len(list1)):
    table.add_row([list1[index], list2[index]])

print(table)
