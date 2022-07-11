


list = [4, 2, 1, 5, 3, 9, 5, 7, 6, 8]
new_list= []
while list:
    min = list[0]
    for i in list:
        if min > i:
           min = i
        
    new_list.insert(0, min)
    list.remove(min)

print(new_list)

