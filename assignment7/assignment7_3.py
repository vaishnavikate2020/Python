class Arithmatic:
    Value=10
    def __init__(self,Number):
        self.n=Number;
        print("Enter Number")
        self.n=int(input())
		
    def chkprime(self):
        flag=False
        if self.n>1:
            for i in range(2,self.n):
                if(self.n%i)==0:
                    flag=True
                    break
        if flag:
            print(self.n,"is not prime")
        else:
            print(self.n,"is prime")
            
    def chkperfect(self):
        
        sum1 = 0
        flag=False
        if self.n>1:
            for i in range(1, self.n):
                if (self.n % i == 0):
                    sum1 = sum1 + i
                if (sum1 == self.n):
                    flag=True
                    break
          
        if flag:
            print(self.n,"is  perfect")
        else:
            print(self.n,"is not perfect")
            
    def print_factors(self):
        print("The factors of",self.n,"are:")
        for i in range(1, self.n + 1):
            if self.n % i == 0:
                print(i)
     
    def printsumfactors(self):
        sum=0
        for i in range(1, self.n + 1):
            if self.n % i == 0:
               sum=sum+i
        print("Addition of factor is {}".format(sum))       
    
def main():
    obj1=Arithmatic(10)
    obj1.chkperfect()
    obj1.chkprime()
    obj1.print_factors()
    obj1.printsumfactors()
    
    obj2=Arithmatic(10)
    obj2.chkperfect()
    obj2.chkprime()
    obj2.print_factors()
    obj2.printsumfactors()
if __name__ == "__main__":
	main()
	