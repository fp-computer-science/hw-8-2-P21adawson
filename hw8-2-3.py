# Azaan Dawson amdg 11/11/20

five_list = input("Enter a 5 numbers seperated by spaces ")
new_list = five_list.split(" ", 4)

num_1 = int(new_list[0])
num_2 = int(new_list[1])
num_3 = int(new_list[2])
num_4 = int(new_list[3])
num_5 = int(new_list[4])

print( num_1 + num_2 + num_3 + num_4 + num_5)
