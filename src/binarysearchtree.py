def binarySearch(myItem, myList):
found= False
bottom=0
top=len(myList)-1
while bottom<=top and not found:
	middle = (bottom + top)//2
if myList[middle]==myItem:
	found=True
elif myList [middle] < myItem:
bottom=middle + 1
else:
top= middle -1

return found

if _name_=="main"
	numberList=[1,45,6,7,8,89,7,8]
	isitFound=binarySearch(item,numberList)
	if isitFound:
		print("ITEM FOUND")
	else:
		print("ITEM NOT FOUND")
