# import argparse
# import sys

# def calc(args):
#     if args.o=="add":
#         return args.x + args.y
#     elif args.o=="sub":
#         return args.x - args.y
#     elif args.o=="mul":
#         return args.x * args.y
#     elif args.o=="div":
#         return args.x / args.y
#     else:
#         return "something went wrong."


# if __name__ == "__main__":
#     parser= argparse.ArgumentParser()
#     parser.add_argument("--x", type=float, default=1.0, help=" Enter first number.This is a utility for calculation. Please contact introvert.")
#     parser.add_argument("--y", type=float, default=3.0, help="Enter second number.This is a utility for calculation. Please contact introvert.")
#     parser.add_argument("--o", type=float, default="add", help="This is a utility for calculation. Please contact introvert  for more.")
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))


import sys
sum=0
# print(sys.argv)
# print(len(sys.argv))
# for ele in sys.argv:
#     print("Argument: ",ele)
for i in range(1, len(sys.argv)):
    sum+=int(sys.argv[i])

print(f"result of sum is {sum}")    