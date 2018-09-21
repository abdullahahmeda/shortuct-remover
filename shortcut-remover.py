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
	# This function scans for all files in a path
	global shortcuts, empty_folders # variables for the number of shortcuts and empty folders

	if os.path.isfile(path): 
		if os.path.splitext(path)[1].lower() == ".lnk": # if the file's extension is .ink, it means it's a shortcut.. so remove this file
			shortcuts += 1
			print("{} is a shortucut virus. removed.".format(os.path.basename(path)))
			os.remove(path)
	else:
		if len(os.listdir(path)) < 1: # if the folder doen't have any file
			try: # to remove it
				empty_folders += 1
				print("{} is an empty folder. removed.".format(path))
				shutil.rmtree(path)
			except: # you don't have the permissions to remove it
				print("can't remove {}".format(path))
		else: # if the folder has files inside it
			for arg in os.listdir(path):
				scan(path + "/" + arg) # scan them

for partition in os.listdir(os.getcwd()): # scan all partitions
	scan(partition)


print("\nFinished!\n\nResults\n------------\nDeleted shortcuts: {}\nDeleted empty folders: {}".format(shortcuts, empty_folders)) # show final output
