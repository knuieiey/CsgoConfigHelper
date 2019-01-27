import shutil
import glob
import os


main_path = os.path.dirname(os.path.realpath(__file__))

paths = []
files = []

for file in os.listdir(main_path):
	if "." not in file:
		paths.append(main_path+"\\"+file+"\\730\\local\\cfg")
	
for file in os.listdir(main_path):
	if file.endswith(".cfg") or file.endswith(".txt"):
		files.append(file)
		
for path in paths:
	if not os.path.exists(path):
		os.makedirs(path)
	for file in files:
		shutil.copy(main_path+"\\"+file, path+"\\"+file)

print("Moved " + str(files) + " to:")
[print(path) for path in paths]