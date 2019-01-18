#Hacking on CSV files!

import csv

import shutil
from tempfile import NamedTemporaryFile
#write a very basic CSV file

#+w means read/or/write and overwrite an existing file or create a new one
with open("templates/data.csv", "w+") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Title", "Description"])
	writer.writerow(["Row 1", "Some descriptionm"])
	writer.writerow(["Row 2", "Some other kind of description"])

# Now to read our file we created in the code block above: 
with open("templates/data.csv", "r") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)

#Using DictReader to open an existing csv file as a dictionary
with open("templates/books.csv", "r") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)

#Using append and DictWriter to add to an existing CSV file w/o overwriting things
with open("templates/books.csv", "a") as csvfile:
	#You have to provide a list of field names to properly map how the CSV will be read/written
	fieldnames = ["title", "author"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writerow({"title": "1984", "author": "George Orwell"})

#as a challenge - try to abscract the last 2 code blocks into their own functions we can call repeatedly to inject data into a csv file.  

def get_lenght(file_path):
	return 1
def append_books(file_path, title, author):
	return []


#Here's how to edit an existing csv file using temp files so 
#you don't accidentally clobber your existing file contents

filename = "templates/books.csv"
tempfile = NamedTemporaryFile(delete=False)

#rb is used for writing/create new
with open(filename, "rb") as tempcsv, tempfile:
	reader = csv.DictReader(tempcsv)
	fieldnames = ["title", "author"]

	#Yes - you need to reference tempfile as your argument here
	writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
	writer.writeheader()

	for row in reader:
		print(row)
		if (row["author"] == ""):
			row["author"] = "Unknown"
		writer.writerow(row)
#This next line copies our temp file to the exiting real file of books.csv
	shutil.move(tempfile.name, filename)

def get_author(author=None):
	filename = 'templates/books.csv'
	with open(filename, "r") as csvfile:
		reader = csv.DictReader(csvfile)
		items = []
		for row in reader:
			if author is not None:
				if author == row.get("author"):
					items.append(row)
		print("Boo yaaaa grandma!")
		print(items)

get_author("George Orwell")