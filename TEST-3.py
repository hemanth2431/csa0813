#square pattern
n=int(input("enter the value:"))
for i in range(1,n+1):
    print("*"*n)


#rectangle pattern
n=int(input("enter the value:"))
for i in range(1,n-1,+1):
    print(" * "*n)


#triangle pattern
n=int(input("enter the value:"))
for i in range(1,n+1,+1):
    print("*"*i)


#diamond pattern
n=int(input("enter the value:"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))

#upper triangle
n=int(input("enter the value:"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))

#lower teiangle
n=int(input("enter the value:"))
for i in range(n-2,-1,-1):
    print(" "*(n-i-1)+"*"*(2*i+1))


#hallow square
n=int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
