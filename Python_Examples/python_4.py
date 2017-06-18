'''
tutorial (4) - function, recursive function, module

2016/06/15

David Hsu
'''

# factorial: f(n) = n!
# function -> def
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def factorialRecursive(n):
    if n == 0 :
        return 1
    else:
        return n*factorialRecursive(n-1)


# fibonacci function : 0, 1, 1, 2, 3, 5, 8, 13, ...
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(3,n+1):
            fib = a+b
            a = b
            b = fib
        return fib

def fibonacciRecursive(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacciRecursive(n-1)+fibonacciRecursive(n-2)

# call by reference or call by value
def doubleList(L):
    L=2*L
    for item in L:
        item *= 2 # item = item*2
    print(L)

def doubleList2(L):
    for i in range(len(L)):
        L[i] *= 2 # item = item*2
    print(L)

def test(x):
    x = x+3
    print(x)

def testStr(s):
    s=s.title()
    print(s)
    
            
        

