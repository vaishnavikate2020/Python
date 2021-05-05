def evnnum(v):
          i=j=1
          while j<=v:
                    if i%2==0:
                              print(i,end=" ")
                              j=j+1
                    i=i+1
def main():
    v=(int(input("Enter number till which you want to print even numbers")))
    evnnum(v)
    
if __name__ =="__main__":
    main()