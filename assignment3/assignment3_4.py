arr = list()
num = input("Enter how many elements you want:")
print ("Enter numbers in array: ")
for i in range(0,int(num)):
        no = input("num :")
        arr.append(int(no))
print ("Entered elements are",arr)
k=0
num=int(input("Enter the number to be counted:"))
for j in arr:
    if(j==num):
        k=k+1
print("Number of times",num,"appears is",k)