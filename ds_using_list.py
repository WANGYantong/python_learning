shoplist=["apple", "mango", "carrot", "banana"]

print("I have {} items to purcharse.".format(len(shoplist)))
print("These items are:", end=' ')
for item in shoplist:
    print(item, end=' ')

print("\nI also hagve to buy rice.")
shoplist.append("rice")
print("My shopping list is now {}".format(shoplist))

print("I will sort my list now")
shoplist.sort()
print("Sorted shopping list is {}".format(shoplist))

print("The first item I will buy is {}".format(shoplist[0]))
olditem=shoplist[0]
del shoplist[0]
print("I bought the {}".format(olditem))
print("My shopping list is now {}".format(shoplist))