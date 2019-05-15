import random
import matplotlib.pyplot as plt

x = []
y = []

def sinDig(x):
    if (x<10):
        return 1
    else:
        return 0

def karastuba(x,y):

    if (sinDig(x) == 1 or sinDig(y) == 1):
        global step
        step = step + 1
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        if(n%2==1):
            n=n-1
        m = n/2
        

        # global step
        # step = step + 1

        a = x/10**(m)
        b = x%10**(m)
        c = y/10**(m)
        d = y%10**(m)

        r0 = karastuba(b,d)
        r1 = karastuba((a+b),(c+d))
        r2 = karastuba(a,c)

        result = (r2*10**(m*2)) + ((r1 - r2 - r0)*10**(m)) + r0

        return result

step = 0

i = 1
while (i<5000):
    m = random.randrange(10**i,10**(i+1))
    n = random.randrange(10**i,10**(i+1))
    global step
    step = 0
    karastuba(m,n)
    print "Number of steps for length of ",i," = ",step
    x.append(step)
    y.append(i)
    i = i*2

# plotting the points  
plt.plot(x,y) 
  
# naming the x axis 
plt.xlabel('steps') 
# naming the y axis 
plt.ylabel('no. of digita') 
  
# giving a title to my graph 
plt.title('Karastuba') 
  
# function to show the plot 
plt.show() 

# m = input("Two number to multiply: ")
# n = input()

# print m," x ",n," = ",karastuba(m,n)
# print "Number of steps = ",step