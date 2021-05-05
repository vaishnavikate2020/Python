import threading 
def NUM (func, lock):
    func (lock)
def Evenfactor (lock):
    lock.acquire()
    sum=0
    num=int(input("Enter number:"))
    for i in range (1, num):
        if num % i == 0 and num%2==0:
            sum=sum+i
    print ("Sum of even factor is {}".format(sum))
    lock.release()
def Oddfactor (lock):
    lock.acquire () 
    sum=0
    num=int(input("Enter number:"))
    for i in range (1, num):
        if num % i == 0 and num%2!=0:
            sum=sum+i
    print ("Sum of odd factor is {}".format(sum))
    lock.release ()
def main ():
    print ("Inside main")
    lock = threading.Lock ()
    t1 = threading.Thread (target = NUM, args =(Evenfactor, lock,))
    t2 =threading.Thread (target = NUM, args =(Oddfactor,lock,)) 
    t1.start ()
    t2.start ()
    t1.join ()
    t2.join ()
    print ("Exit from main")
if __name__== "__main__":
    main ()
