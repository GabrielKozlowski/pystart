import argparse

parser = argparse.ArgumentParser(
    prog='Arg_Parse',
    description='This Program Print ArgParse',
    epilog='Gabriel'
)

parser.add_argument('path', type=str)
parser.add_argument('target', type=str)
parser.add_argument('-wi', '--width', default=300, type=int)
parser.add_argument('-he', '--height', default=300, type=int)


args = parser.parse_args()
print(args.path)
print(args.target)
print(args.width)
print(args.height)
print(args.height * args.width)