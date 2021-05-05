import threading 
def NUM (func, lock):
    func (lock)
def Even (lock):
    lock.acquire () 
    print("Even numbers:")
    for i in range (1, 11):
        if i % 2 == 0:
            print (i)
    lock.release()
def Odd (lock):
    lock.acquire () 
    print("Odd Numbers:")
    for i in range (1, 11):
        if i % 2 != 0:
            print (i)
    lock.release ()
def main ():
    print ("Inside main")
    lock = threading.Lock ()
    t1 = threading.Thread (target = NUM, args =(Even, lock,))
    t2 =threading.Thread (target = NUM, args =(Odd,lock,)) 
    t1.start ()
    t2.start ()
    t1.join ()
    t2.join ()
    print ("End of main")
if __name__== "__main__":
    main ()
