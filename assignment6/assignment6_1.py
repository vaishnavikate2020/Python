class Demo:
    value=100
    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2
        
    def Fun(self):
        print(self.i)
        print(self.j)
    def Gun(self):
        print(self.i)
        print(self.j)

def main():
    print("value is:",Demo.value)
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj1.Gun()
    Obj2.Fun()
    Obj2.Gun()

if __name__=="__main__":
    main()
