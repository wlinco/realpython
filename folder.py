import os

my_path = "/home/will/code/python/realpython"

my_input_file = open(os.path.join(my_path, "hello.txt"), "r")

print my_input_file.readlines()

filename_list = os.listdir(my_path)

for filename in filename_list:
	print filename
