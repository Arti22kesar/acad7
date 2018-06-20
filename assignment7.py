#Ques1.

radius=float(input("enter the no"))
def area(rad):
    area=3.14*rad*rad
    return area
ar=area(radius)
print(ar)


#Ques2.

n=6
def perfect(n):
   sum=0
   for i in range(1,n):
        if(n%i==0):
            sum=sum+i
   if(sum==n):
     return True
   else:
     return False
for i in range(1,1001):
    if(perfect(i)==True):
        print(i)

#Ques3.

def mul_table(n, i=1):
    print(n*i)
    if(i !=10):
        mul_table(n,i+1)
print(mul_table(12))

#Ques4.

def power(a,b):
    if b == 1:
        return a
    else:
        return a*power(a,b-1)
print(power(6,2))

#Ques5.

def fact(n):
    if (n<=1):
        return 1
    else:
        return n * fact(n-1)
d={}
n=int(input("enter no:"))
print("fact:")
print(fact(n))
d[n]=fact(n)
print(d)




