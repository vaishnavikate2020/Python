def Prime(n):
          i=2
          j=0
          while i<n:
                    if n%i==0:
                              k=1
                    i=i+1
          return j

def main():
	x=(int(input("Enter the  number")))
	y=Prime(x)
	if y==1:
			print("Not Prime")
	else:
			print(" Prime")

if __name__ =="__main__":
			main()
