import random

def sinDig(x):
    if (x<10):
        return 1
    else:
        return 0

def dnq(x,y):

    if (sinDig(x) == 1 or sinDig(y) == 1):
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        if(n%2==1):
            n=n-1
        m = n/2
        

        global step
        step = step + 1

        a = x/10**(m)
        b = x%10**(m)
        c = y/10**(m)
        d = y%10**(m)

        ac = dnq(a,c)
        ad = dnq(a,d)
        bc = dnq(b,c)
        bd = dnq(b,d)

        result = ac*10**(n) + (ad + bc)*10**(n/2) + bd

        return result

step = 0
i = 1
while (i<5000):
    m = random.randrange(10**i,10**(i+1))
    n = random.randrange(10**i,10**(i+1))
    dnq(m,n)
    # print m," x ",n," = ",dnq(m,n)
    print "Number of steps for length of ",i," = ",step
    i = i*2

# m = input("Two number to multiply: ")
# n = input()

# print m," x ",n," = ",dnq(m,n)
# print "Number of steps = ",step