def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list

list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
print ("Initial list", list) #if written after calling the function it will return the list containing numbers less than 20
num_list_sub_20 = numbers_less_than_twenty(list) #function call 
print ("List that doesn't contain numbers greater than 20", num_list_sub_20) #printing after the operations are done 