n=10
for i in range(1, n+1):
    print(i)
def sum_of(n):
    return (n*(n +1))// 2
sum_natural = sum_of(n)
print(f"sum of n natural numbers: {sum_natural}")

x=4
for i in range (x,0,-1):
    print(i)

odd=[num for num in range(1,n)if num%2!=0]
print(odd)

even=[num for num in range(1,n)if num%2==0]
print(even)

def sum_even_numbers(n):
    total_sum = 0
    num = 2
    for _ in range(n):
        total_sum += num
        num += 2
    return total_sum


def sum_of_digits(n):
    total=0
    for digit in str(n):
        total+=int(digit)
    return total
n=123
result=sum_of_digits(n)
print(f"the sum of digits is: {result}.")


print("Addition is {}".format(add()))

def reverse_digits(num):
    return int(str(num)[::-1])
num=123
reversed_number = reverse_digits(num)
print(f"The reversed number is: {reversed_number}")

n = int(input("Enter the number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")



a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
for i in range(a,b+1):
        if i>1:
            count=0
            for j in range(1,i+1):
                if i%j==0:
                    count=count+1
            if count==2:
                print("prime number b/w",a,"and",b,"=",i)



def add():
    n1 = int(input("Enter the Number 1:"))
    n2 = int(input("Enter the Number 2:"))
    print("Addition of {} + {} is {}".format(n1, n2, (n1 + n2)))
add()

def add(n1, n2):
    print("subtraction of {} + {} is {}".format(n1, n2, (n1 - n2)))

a = int(input("Enter the Number 1: "))
b = int(input("Enter the Number 2: "))
add(a, b)
