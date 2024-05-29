# Chaining Decorators
# In simpler terms chaining decorators means decorating a function with multiple decorators.

# Example:


def decorator1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decorator2(func):
    def inner():
        x=func()
        return x*9
    return inner

@decorator1
@decorator2
def num1():
    return 4

@decorator1
@decorator2
def num2():
    return 9

print(num1())
print(num2())
    


# What if a function returns something or an argument is passed to the function?
   

def hello_decorator(func):
    def inner(*args, **kwargs):
        print("before execution")
        returned_value=func(*args,**kwargs)
        print("after execution")
        return returned_value
    return inner

@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
 
a, b = 1, 2
 
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))   