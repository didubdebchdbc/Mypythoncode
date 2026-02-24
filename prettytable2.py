
#n Mazzetti
#pretytable2
#08.10.2025

items =  []
quantity = []
cost = []

item = ""
itemQ=0                   # making a variable
itemP=0

while (item!= "done"):
    item = input("Enter item")

    if(item == "done"):
        break       #QUIT THE LOOP

    itemQ = input("Enter item qunatity")

    itemP = float(input("Enter item price £"))

    items.append(item)              #add something to a list
    quantity.append(itemQ)
    cost.append(itemP)


print(items)
print(quantity)
print(cost)

