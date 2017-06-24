#!/usr/bin/python

import os
import shutil

# used methods:
# os.path.splitext(file): returns an array, the first index is the dirname. the second one is the file extension.
# os.path.isfile(arg): chek if the argument is file or not, returns true if so. and false if not.
# os.path.isdir(arg): chek if the argument is folder or not, returns true if so. and false if not.
# os.listdir(place): returns a list of all files and folders in the given place.
# os.path.abspath(arg): retruns the path of the given argument

partitions_place = "/media/abdullah/"
os.chdir(partitions_place)

shortcuts = 0
empty_folders = 0

def scan(path):
	global shortcuts, empty_folders

	if os.path.isfile(path):
		if os.path.splitext(path)[1].lower() == ".lnk":
			shortcuts += 1
			print("{} is a shortucut virus. removed.".format(os.path.basename(path)))
			os.remove(path)
	else:
		if len(os.listdir(path)) < 1:
			try:
				empty_folders += 1
				print("{} is an empty folder. removed.".format(path))
				shutil.rmtree(path)
			except:
				print("can't remove {}".format(path))
		else:
			for arg in os.listdir(path):
				scan(path + "/" + arg)

for partition in os.listdir(os.getcwd()):
	scan(partition)


print("\nFinished!\n\nResults\n------------\nDeleted shortcuts: {}\nDeleted empty folders: {}".format(shortcuts, empty_folders))
