from sympy import randprime

x = randprime(100,1000)
y = randprime(100,1000)
print("x: ",x,"\ny: ",y)
print(f"x+y: {x+y}")
print(f"x-y: {x-y}")
print(f"x*y: {x*y}")
print(f"x/y: {x/y}")
print(f"x^y: {pow(x,y)}")