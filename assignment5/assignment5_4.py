sum = 0
i = 0
def AddtionR(data):
    global sum
    global i
    if i < len(data):
        sum = sum + data[i]
        i = i + 1
        AddtionR(data)
    return sum

    
def main():
    arr = []
    size = int(input("Enter the size of array"))
    for i in range(size):
        arr.append(int(input()))
        
    print("Data is : ",arr)
    
    print("Addition is ",AddtionR(arr))
if __name__ == "__main__":
    main()