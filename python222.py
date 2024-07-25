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
