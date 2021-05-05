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
	
    even = list(filter(lambda no:  no%2==0, arr))
    print("After filtering data is :",even)
    mod = list(map(lambda no: no**2, even))
    print("After map data is :",mod)
    sum = reduce(lambda a, b: a + b, mod)
    print("After reducing data:",sum)
    
if __name__=='__main__':
    main();
