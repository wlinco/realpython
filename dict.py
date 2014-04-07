my_dict = {"luke":"5/24/19","obiwan":"9/3/09","vader":"9/1/10"}

if "yoda" not in my_dict:
	my_dict["yoda"] = "2/2/2"

if "vader" not in my_dict:
	my_dict["vader"] = "3/3/3"

for name in my_dict:
	print name + " " + my_dict[name]

del(my_dict["vader"])

print my_dict

other_dict = dict([("luke","1/1/1"), ("vader", "2/2/2")])

print other_dict
