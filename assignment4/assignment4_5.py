from functools import reduce
def prime(num):
   for j in range(2, num):
      if num % j == 0:
         return False
   else:
      return True

def main():
    arr = []
    print("Enter number of elements")
    size = int(input())
    
    for i in range(size):
        print("Enter element number :",i+1)
        no = int(input())
        arr.append(no)
        
    print("Your entered data is :",arr)
	
    primearr = list(filter(prime, arr))
    
    print("after filtering data is: ",primearr)
    
    modarr = list(map(lambda no: no*2, primearr))
    print("After mapping data is: ",modarr)
    
    sum = reduce(lambda x,y: x if x > y else y, modarr)
    print("After reduce data is: ",sum)

	
if __name__=='__main__':
    main();

