#string to integer
a=str(input("enter a string:\n"))
result=int(a)
print("result:",result)

#remove duplicate elements
a=eval(input("enter the list:\n"))
result=set(a)
print(list(result))

#average of list of integers
a=eval(input("enter the list:\n"))
sum=0
length=len(a)
for i in a:
    sum=sum+i
average=sum/length
print("average list of integers:\n",average)

#perfect square(or)not
import math
a=int(input("enter the square of a number:\n"))
result1=math.sqrt(a)
result2=result1**2
if result2==a:
    print("perfect square")
else:
    print("not a perfect square")

#sum of all even numbers in a list
a=eval(input("enter the list"))
sum=0
for i in a:
    if i%2==0:
        sum=sum+i
print(sum)
