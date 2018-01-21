def OddEven():
    for i in xrange(1, 2001, 1):
        mod = i % 2
        if mod > 0:
            print("Number is "+str(i)+" is an odd number.")
        else:
            print("Number is "+str(i)+" is an even number.")	


OddEven()

def Multiply(a,b):
    z=len(a)
    for x in a[:]:
        y= x*b
        print y

Multiply([3,5,7,8,9],5)

def layered_multiples(a,b):
    list1=[]
    list2=[]
    z=len(a)
    for x in a[:]:
        y = x*b
        list1 = [1]*y
        list2.append(list1)
            
        print list2
 

layered_multiples([3,5,7,9,],5)