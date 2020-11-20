# Azaan Dawson amdg 11/11/20

og_list  = input("please enter a list of number or letters seperated by spaces ")
selection = input("enter middle (all lowercase) if you want the middle or end (all lowercase) if you want the ends")

new_list = og_list.split(' ')

length = int(len(new_list))

list_middle = new_list[1:length -1]
list_ends = new_list[0] + new_list[length- 1]

if selection == 'middle' :
  print((list_middle))
elif selection == 'end':
  print(list_ends)
else:
  print("error!!")
