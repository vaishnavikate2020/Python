from functools import reduce

def main():
    arr = []
    print("Enter number of elements")
    size = int(input())
    
    for i in range(size):
        print("Enter element number :",i+1)
        no = int(input())
        arr.append(no)
        
    print("Your entered data is :",arr)



    Arr1 = list(filter(lambda no:  no>=70 and no<=90, arr))
    print("After filtering data is :",Arr1)
    addArray = list(map(lambda no: no + 10, Arr1))
    print("After map data is :",addArray)

    product = reduce(lambda a, b: a * b, addArray)
    print(product)


if __name__=='__main__':
    main();
