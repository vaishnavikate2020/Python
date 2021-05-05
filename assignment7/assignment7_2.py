class BankAccount:
    ROI=10.5
    def __init__(self,Name,Amount):
        self.n=Name;
        self.a=Amount;
        print("Enter Name")
        self.n=(input())
        print("Enter Amount")
        self.a =int(input())
    def deposit(self,depo):
        print("Enter amount to be deposited")
        self.depo=int(input())
        self.a+=self.depo
    
    def Withdraw(self,depo):
        print("Enter amount to be withdraw")
        self.withd=int(input())
        self.a-=self.withd
        
    def simpleinterest(self,time):    
        simple_interest = (self.a * time * BankAccount.ROI) / 100
        print("The simple interest is:", simple_interest)

    
    def display(self):
        print("Name of account holder is",self.n)
        print("Amount in account",self.a)
def main():
    obj1=BankAccount("Vaishnavi",10000)
    obj1.deposit(3000)
    obj1.display()
    obj1.Withdraw(2000)
    obj1.display()
    obj1.simpleinterest(2)
    obj1.display()
    
    obj2=BankAccount("Vaishnavi",10000)
    obj2.deposit(3000)
    obj2.display()
    obj2.Withdraw(2000)
    obj2.display()
    obj2.simpleinterest(2)
    obj2.display()
if __name__ == "__main__":
	main()
