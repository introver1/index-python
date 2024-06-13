from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument("echo", help="Echos the given string")


args:Namespace = parser.parse_args()

print(args.echo)