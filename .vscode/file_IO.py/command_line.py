# creating command line utility in python



import argparse 
parser = argparse.ArguementParser()


# Add command line arguements
parser.add_arguement("url", help="Url of the file to download")
parser.add_arguement("outpput", help="by which do you want to save your file")


# Parse the arguements
args = parser.parse_args()

# Use the arguement in your code
print(args.url)
print(args.output)