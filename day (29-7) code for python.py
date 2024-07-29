a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d = b*b-4*a*c
if d>0:
    print("The roots are real and different.")
elif d==0:
    print("The roots are real and the same.")
else:
    print("The roots are imaginary.")


a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if(a>b):
    if(a>c):
        print("the greatest no is ",a)
    else:
        print("the greatest no is ",c)
else:
    if(b>c):
        print("the greatest no is ",b)
    else:
        print("the greatest no is ",c)

num=int(input("Enter a number: "))
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10

if num==sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


n =int(input("enter the number:"))
for i in range(1,n,1):
    if(i%5==0 and i%10!=0):
        print(i)

n=int(input("enter the number:"))
for i in range(1,n+1,1):
    if(n%i==0):
        print(i)
n = int(input("enter a number: "))
sum = 0
for i in range(1,n,1):
    if n%i== 0:
        sum=sum+i
if sum==n:
    print("it is a perfect number.")
else:
    print("it is not a perfect number.")

n = 100
for num in range(1,n,1):
    count=0
    for i in range(1,num+1,1):
        if num%i==0:
            count=count+1
    if count==2:
        print(num)
