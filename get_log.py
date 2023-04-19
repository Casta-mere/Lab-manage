import os
import re

path="d:\CODE\python"

# get the path of the current file
# path = os.path.dirname(os.path.abspath(__file__))

# print(path)

# get all the files in the current directory
files = os.listdir(path)


name="get"

# get all the files that start with "get"
files = [f for f in files if re.match(name, f)]

print(files)

# open folder in explorer
os.startfile(path)