class Bookstore:
    NoofBooks=0
    def __init__(self,Name,Author):
        self.n=Name
        self.a=Author
        print("Enter Name of book:")
        self.n=(input())
        print("Enter Author of book:")
        self.a =(input())
        Bookstore.NoofBooks+=1
        

    def Display(self):
        print("Name of Book is:",self.n)
        print("Author of Book is:",self.a)
        print("Number of Books is:",self.NoofBooks)
def main():
    obj1=Bookstore("Linux System Programming", "Robert Love")
    obj1.Display()
    
    obj2=Bookstore("C Programming","Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
	main()