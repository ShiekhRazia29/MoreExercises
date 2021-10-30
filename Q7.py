#items in both the lists
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
new_list=[]
for i in (list1 and list2):
  if i  in (list1 or list2):
      new_list.append(i)
print("New list will be",new_list)