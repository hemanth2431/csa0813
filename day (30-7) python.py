#multiplication table
def multi(n):
    for i in range(1, 11):
        print(f"{n}*{i}={n * i}")
multi(5)

#sum_of_n_natural_numbers
def sum_of_n_numbers(num):
    return (num*(num+1))//2
n=10
result=sum_of_n_numbers(n)
print(f"Sum of first {n} natural numbers is: {result}")

#convert string to intiger
def convert_to_int(num_str):
    return int(num_str)
num_str = "30"
num_int = convert_to_int(num_str)
print(num_int)

#tuple to list
def x(tuple):
    return(x)
tuple=(1,2,3)
x=list(tuple)
print(x)

#list to tuple
def f(string):
    return(f)
string="25"
f=float(string)
print(f)

#string to float
def f(string):
    return(f)
string="50"
f=float(string)
print(f)

#LCM of a two nubers
def lcm(n1, n2):
    greater = max(n1, n2)  
    for i in range(greater, (n1 * n2) + 1):
        if i % n1==0 and i%n2==0:
            return i
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
print("The LCM is:",lcm(n1,n2))


#remove duplicends
def remove_duplicates(arr):
    return list(set(arr))
array = [1, 2, 2, 3, 4, 4, 5]
unique_array = remove_duplicates(array)
print(unique_array)


