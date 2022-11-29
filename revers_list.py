list1=[10,34,52,67,3,12,9]
list2=[]
len=len(list1)
for i in range(len-1,-1,-1):
    list2.append(list1[i])
print(list2)