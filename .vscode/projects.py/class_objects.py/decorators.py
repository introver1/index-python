

# def outer_function(x):
#     def  inner_function(y):
#         return x+y
#     return inner_function
# add_function=outer_function(5)
# # print(add_function)
# result=add_function(6)
# print(result)


# Pass Function as Argument
# We can pass a function as an argument to another function in Python. For Example,

# def add(x, y):
#     return x+y
# def calculate(func,x, y):
#     return func(x, y) 
# result =calculate(add,8,9)
# print(f"The addition of variable x and y passing function as argumrnt is {result}")


# def sub(a,b):
#     return a-b
# def calculation(func, a, b ):
#     return func(a, b)
# result1=calculation(sub, 9, 6)
# print(f"The subtraction of variable a and b passing function as argumrnt is {result1}")


# Return a Function as a Value
# In Python, we can also return a function as a return value. For example,


# def greet(name):
#     def hello():
#         return "hello, "  + name
#     return hello
# greeting=greet("Introvert")
# print(greeting())




# def make_pretty(func):
#     # define the inner function 
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")

#         # call original function
#         func()
#     # return the inner function
#     return inner

# # define ordinary function
# def ordinary():
#     print("I am ordinary")
    
# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)

# # call the decorated function
# decorated_func()


# def make_pretty(func):
#     def inner_function():
#         print("This is inner function")
#         func()
#     return inner_function

# @make_pretty
# def decorate_function():
#     print("Hi, i am a decorator.")
# decorate_function()
    

# def smart_divide(func):
#         print("We are going to print the division of",a,"and", b )
#         if b==0:
#             print("oops cant divide")
#             return
#         return func(a,b) 
#     return smart_divide
# @smart_divide
# def divide(a,b):
#     print(a/b)
# divide(8,4)      
# def inner_func(a, b):
   

# import time
# import math

# def calculate_time(func):
#     def inner_function(*args,**kwargs):
#         begin=time.time()
#         func(*args, **kwargs)
#         end=time.time()
#         print("Total time taken in",func.__name__, begin - end)
#         return inner_function
    
# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))   

# factorial(5)    




# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
	
	# added arguments inside the inner1,
	# if function takes any arguments,
	# can be added like this.
	def inner1(*args, **kwargs):

		# storing time before function execution
		begin = time.time()
		
		func(*args, **kwargs)

		# storing time after function execution
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)

	return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))

# calling the function.
factorial(10)
