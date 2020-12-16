# def print2(str1):
#     print2(str1)
#     print("this is",+str1)
# print2("shiv")
"""factorial_iterative
def factorial(n):
    fac=1
    for i in range(n):
        fac= fac*(i+1) 
    return fac

number = int(input("enter the number"))
print(factorial(number))
#factorial using altartive method
"""

#fatorial_recursive
# def factorial_recursive():
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# number=int(input("enter the number"))
# print("factorial using recursive method",factorial_recursive)

def factorial(number):#factorial_iterative
    product=1
    for i in range(number):
        product = product*(i+1)
    return product
number=int(input("enter the number"))
print("factorial_iterative",factorial(number))

def factorial2(number2):
    product2=1
    for j in range(number2):
        product2 =product2*(j+1)
    return product2
number2=int(input("enter the number2"))
print("factorial_iterative2",factorial2(number2))

d=(factorial(number)+factorial2(number2))
print("sthe sum of the factorial1 and factorial2 is =",d)
def factorial3(d):
    product3=1
    for p in range(d):
        product3=product3*(p+1)
    return product3
print("factorial_iterative",factorial3(d))
#factorila_recursive
# def factorial(number):
#     if number <=1:
#         return 1
#     else:
#         return number*factorial(number-1)
# number=int(input("enter the number"))
# print("the factorial recursion is",(factorial))"""