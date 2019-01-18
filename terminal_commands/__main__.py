#This is the main class

#This lets us parse terminal arguments for python
from argparse import ArgumentParser
import os

findauthor = "George Orwell"
filename = None
file_path = None

parser = ArgumentParser(prog="terminal_madness")
parser.add_argument('--user', type=str)
parser.add_argument('--file', type=str)
args = parser.parse_args()

if args.user is not None:
	print(args.user)

if args.file is not None:
	filename = args.file
	file_path = os.path.join(os.path.get_cwd(), filename)
	#This is another way of accomplishing the same thing on the line above
	#file_path = os.path.join(os.path.dirname(__file__), filename)

try:
	if not os.path.isfile(file_path):
	      raise Exception("The file path specified invalid: %s"%(file_path))
except Exception:
    print("File is not defined")
try:
	with open(file_path, "r") as csvfile:
		reader = csv.DictReader(csvfile)
		items = []
		for row in reader:
			if findauthor == row.get('author'):
				items.append(row.get('title'))
		print(items)
except Exception:
	print("This thing's broken, yo")
