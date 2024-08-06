def string():
    a=input("enter a string:")
    string_reverse=a[::-1]
    return string_reverse
reverse=string()
print("reversed String:",reverse)


def multi(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
multi(5)

def anagram(x,y):
    x=x.lower()
    y=y.lower()
    return sorted(x)==sorted(y)
x=input("enter the first word : ")
y=input("enter the second word : ")
if anagram(x,y):
    print(x,"and",y,' are anagrams')
else:
    print(x,"and",y,'are not anagrams')



def numbers(a):
    return(a)
a=[10,50,20,40,30,60,90,70,80]
a.sort()
print("Ascending order is ", a)
print("Descnding order is ", a[::-1])


#Dfference 
a=[1,8,3,4,5]
b=[1,2,6,4,5]
diff=list(set(a)-set(b))
print(diff)


#star pattern 1(square)
n=int(input("enter the value of n:\n"))
for i in range(1,n+1):
       print("*"*n)

       
#star pattern 2(triangle)
n=int(input("enetr the value of n:\n"))
for i in range(1,n+1,+1):
        print("*"*i)


#star pattern 3(rectangle)
n=int(input("enter the value:\n"))
for i in range(1,n-1,+1):
      print(" * "*n)

#star pattern 4(hello square)
n=int(input("Enter the value:\n"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

#star pattern 5(diamond)
n=int(input("enter the value:\n"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))

#star pattern 6(upper triangle)
n=int(input("enter the value:\n"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))

#star pattern 7(lower triangle)
n=int(input("enter the value:\n"))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))


