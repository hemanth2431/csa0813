#marks Grading:

  marks=int(input("enter the marks:"))
if marks>=90:
    print("you got S grade")
elif marks>=80:
    print("you got A grade")
elif marks>=70:
    print("you got B grade")
elif marks>=60:
    print("you got C grade")
elif marks>=50:
    print("you got D grade")
else:
    print("you got F grade")

#crate a list:
    
num=[1,2,3,4,5,6]
      
num.append(3)
      
print(num)
      
[1, 2, 3, 4, 5, 6, 3]
num=[1,2,3,4,5]
      
num2=[5,6,7,8,9]
      
print(num)
      
[1, 2, 3, 4, 5]
print(num2)
      
[5, 6, 7, 8, 9]
print(num[0])
      
1
print(num[3])
      
4
print(num2[3])
      
8
print(num[1:3])
      
[2, 3]
print(num2[2:4])
      
[7, 8]
print(num[1:])
      
[2, 3, 4, 5]
print(num+num2)
      
[1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
print(num*2)
      
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
num[2]=45
      
print(num)
      
[1, 2, 45, 4, 5]
num.insert(2,"program")
[1, 2, 'program', 45, 4, 5]
num2.remove(45)
      
print(num)
      
[1, 2, 'program', 4, 5]

#bitwise operator:

a=12
b=13
a&b
12
a|b
13
12^13
1
10>>2
2
~12
-13

#arthamatic operations:

a=3
      
b=9
      
print(a+b)
      
12
print(b-a)
      
6
print(b/a)
      
3.0
print(a/b)
      
0.3333333333333333
print(a*b)
      
27
print(a//b)
      
0
print(b%a)
      
0
print(a%b)
      
3
print(a^b)
      
10
print(a**b)
      
19683

#Assignment operatot:

a=10
b=20
c=a+b
print(c)
30
c+=a
print(c)
40
c-=a
print(c)
30
c*=a
print(c)
300
c/=a
print(c)
30.0
c/=a
print(c)
3.0
c%=a
print(c)
3.0
c**=a
print(c)
59049.0
c//=a
print(c)
5904.0
