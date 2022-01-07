"""
CodeLibrary.argparse_eg
~~~~~~~~~~~~~~~~~~~~~~~

Function: 命令行选项、参数和子命令的解析器

Crater: lin
CreateDate: 2022-01-06
"""
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("echo", help="echo the String you ues here")
parser.add_argument("num", help="echo the String you ues here", type=int)

parser.add_argument("-v", "--version", help="--version", action="store_true")
parser.add_argument("-c", help="all_count", action="count", default=95)

args = parser.parse_args()

print("Hello, %s." % args.echo)
if args.num > 9:
    print("The num ori is %s, *10 after change %s" % (args.num, args.num * 10))
else:
    print("The num ori is %s, not change" % args.num)
if args.version:
    print("version 0.1.520")
print(args.c)