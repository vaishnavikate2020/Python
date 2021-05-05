def strname(v):
          icnt=0
          for i in v:
                    icnt=icnt+1
          print("String length is {}".format(icnt))

def main():
	v=input("Enter string")
	strname(v)

if __name__ == "__main__":
	main()