# Closures 
# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Let us get to it step by step 

# def transmit_to_space(message):
#     "This is the enclosing function"
#     def data_transmitter():
#         "The nested function"
#         print(message)

#     data_transmitter()

# print(transmit_to_space("Test message"))

# This works well as the 'data_transmitter' function can access the 'message'. To demonstrate the use of the "nonlocal" keyword, consider this

# def print_msg(number):
#     def printer():
#         "Here we are using the nonlocal keyword"
#         nonlocal number
#         number=3
#         print(number)
#     printer()
#     print(number)

# print_msg(9)

# def main_func(messege):
#     def inside_func():
#         print(messege)
#     return inside_func
# func1= main_func("Burn the sky, to light the world")    
# func1()


# # Exercise
# Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures.
# That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.


# def multiplication_of(n):
#     def multiplier(number):
#         return number*n
#     return multiplier
# multiplication_with5=multiplication_of(5)
# print(multiplication_with5(6))


# Example: Print Odd Numbers using Python Closure
def outer_func():
    num=1
    def inner_func():
        nonlocal num
        num += 2
        return num 
    return inner_func
odd = outer_func()
print(odd())
print(odd())
print(odd())
print(odd())
print(odd())
print(odd())