p=10
n=8
r=15
a=(p*n*r)/100
print(a)

p=int(input("enter value:"))
t=int(input("enter value:"))
r=int(input("enter value:"))
amt=p*(pow(1+(r/100),t))
print(amt)
ci=amt-p
print(ci)

set1={1,6,3,4}
set2={5,6,7,8}
union=set1|set2
print(union)
intersection=set1&set2
print(intersection)

str="hemanth"
print(len(str))

x=[3,7,5,1,4,2]
print(sorted(x))
x.sort(reverse=True)
print(x)

list1={1,3,7,5,3}
print(list(set(list1)))

n=5
fact=1
for i in range (1,n+1):
    fact=fact*i
print(fact)

n=5
if n%2==0:
    print("even")
else:
    print("odd")

a=int(input("enter value:"))
if(a%4==0):
    print("leap year")
else:
    print("not leap year")

a=int(input("enter value:"))
b=int(input("enter value:"))
c=int(input("enter value:"))
if(a>b):
    print("a is grater")
if(c>a):
    print("c is grater")
else:
    print("b is grater")

n=int(input("enter the no.of terms:"))
ft=0
st=1
nt=0
for i in range(0,n+1):
      ft=st
      st=nt
      nt=ft+st
      print(nt)
        
