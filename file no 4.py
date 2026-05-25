myList = ["apple", "banana", "cherry","watermellon"]
myList.remove("watermellon")
print(myList)
myList = ["apple", "banana", "cherry","watermellon"]
myList.remove("apple")
print(myList)
myList = ["apple", "banana", "cherry","watermellon"]
for i in range (len(myList)):
    print(myList[i])
myList = ["apple", "banana", "cherry", "watermellon"]
while myList:
    removed = myList.pop(0)
    print("Removed:", removed)
    print("Remaining List:", myList)

    myList = ["apple", "banana", "cherry", "watermellon"]
    for i in myList[:]:
        print("deleted",myList)
        print(myList.remove(i))
    print (myList)
myList = ["apple", "banana", "cherry", "watermellon"]
print(myList.append("mango"))
print(myList)
myList = ["apple", "banana", "cherry", "watermellon"]
newlist = []
for i in myList:
    newlist.append(i)
print(newlist)
myList = ["apple", "banana", "cherry", "watermellon"]
a = [x for x in myList]
print(a)
myList = ["apple", "banana", "cherry", "watermellon"]
a = [i for i in  myList if i == "apple" ]
print(a)
myList = ["apple", "banana", "cherry", "watermellon"]
for i in myList:
    print(i.upper())
myList = ["apple", "banana", "cherry", "watermellon"]
myList.sort()
print(myList)