total=0
arr = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
for i in range(0,int(num)):
        no = input("num :")
        arr.append(int(no))
print ("Entered elements are",arr)
for ele in range(0, len(arr)):
    total = total + arr[ele]
print("Sum of all elements in given list: ", total)