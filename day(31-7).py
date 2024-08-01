#indexing
s=str(input("enter the string\n"))
print(s[1])
print(s[3])

#slicing
s=str(input("enter the string\n"))
print(s[0:2])


s=str(input("enter the string\n"))
print(s[::-1])

s1=str(input("enter the first string\n"))
s2=str(input("enter the second string\n"))
print(s1+s2)

s=str(input("enter the string\n"))
print(s*4)

#capitalize
s=str(input("enter the string\n"))
print(s.capitalize())
    
#upper
s=str(input("enter the string\n"))
print(s.upper())
    
#Lower
s=str(input("enter the string\n"))
print(s.lower())
    
#title
s=str(input("enter the string\n"))
print(s.title())
    
#swapcase
s=str(input("enter the string\n"))
print(s.swapcase())
    
#split
s=str(input("enter the string\n"))
print(s.split())
    
#count
s=str(input("enter the string\n"))
print(s.count("hello"))
    
#center
s=str(input("enter the string\n"))
print(s.center(19,"*"))
    
#replace
s=str(input("enter the string\n"))
print(s.replace("hello","hi"))
    
#join
a=str(input("enter a string\n"))
b=str(input("joining a string\n"))
print(b.join(a))

#ISupper
s=str(input("enter a string\n"))
print(s.isupper())

#islower
s=str(input("enter a string\n"))
print(s.islower())

#isalpha
s=str(input("enter a string\n"))
print(s.isalpha())

#isalnum
s=str(input("enter a string\n"))
print(s.isalnum())

#isdigit
s=str(input("enter a string\n"))
print(s.isdigit())

#punctuation
import string
print(string.punctuation)

#string digits
import string
print(string.digits)

#string printable
import string
print(string.printable)

#string capwords
import string
print(string.capwords("hello"))

#stringhexdigits
import string
print(string.hexdigits)

#octdigits
import string
print(string.octdigits)

#import array
import array
sum=0
a=array.array('i',[1,2,3,4,5])
for i in a:
    sum=sum+i
print(sum)

#convert list into sum of array
import array
sum=0
x=[1,2,3,4,5]
a=array.array('i',[])
a.fromlist(x)
for i in a:
    sum=sum+i
print(sum)
