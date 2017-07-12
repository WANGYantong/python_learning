print("Simple Assignment")
shoplist=["apple","mango","carrot","banana"]
mylist=shoplist

shoplist.remove("apple")
print("shoplist is {}".format(shoplist))
print("mylist is {}".format(mylist))

mylist=shoplist[:]
del mylist[0]
print("shoplist is {}".format(shoplist))
print("mylist is {}".format(mylist))
