arr = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
for i in range(0,int(num)):
        no = input("num :")
        arr.append(int(no))
print ("Entered elements are",arr)
print("Largest element is:", max(arr)) 