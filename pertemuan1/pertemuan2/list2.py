thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#len
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list item-tipe data
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#campuran tipe data
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#Konstruktor list()
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#menambahkan list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #negatif index

#menukar item list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#append item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

