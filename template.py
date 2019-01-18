#this is a template file

#allows OS file systems to work well within python code
import os

file_ = 'templates/mytemplate.txt'
context = {
	"name": "Toby",
	"date": "ABC",
	"thing": "Cheeseburgers"
  }

def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
      raise Exception("Template file path invalid: %s"%(file_path))
    return file_path

print(get_template_path(file_))

def get_template(path):
  file_path = get_template_path(path)
  return open(file_path).read()

# ** indicates that we are formatting with a dictionary  
print(get_template(file_).format(**context))