list1=[3,12,87,12,39,12,12,51,87,39]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

