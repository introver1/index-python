import argparse, datetime

parser=argparse.ArgumentParser(description="A random program that does something")
parser.add_argument("filename",nargs="*", default="file1.txt", help="filename to be processed.")
parser.add_argument("-c","--copy", nargs="?", default=1, const=2)
parser.add_argument("-s","--something", action="count", default=0)
parser.add_argument("-v","--version",dest="list_values", action="version", version="parse1.py v2.01")
parser.add_argument("-n","--name",default="file_copy",choices=["name_1","name_2"] )
arguments=parser.parse_args()
print(arguments)

