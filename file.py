my_output_file = open("hello.txt", "a")

lines_to_write = ["line1", "line2"]

my_output_file.writelines(lines_to_write)

my_output_file.close()

my_input_file = open("hello.txt", "r")

for line in my_input_file.readlines():
	print line,


my_input_file.close()

with open("hello.txt", "r") as my_input_file:
	print my_input_file.readlines()
