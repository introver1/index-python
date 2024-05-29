# To calculate the sum of first naturals numbers.
def sum_natural_numbers(n):
    sum=0
    while n>0:
        print(n)
        sum = sum + n
        n = n - 1
    print(sum)
sum_natural_numbers(9)        


# To print all elements in a list using ewcursive function
# def print_list(list,idx=0):
#     while idx== len(list):
#         print(list[idx])
#         print_list(list,idx+1)
# lst1=["laddu",'rasbari',"gulab jamun","peda"]
# print_list(lst1)        