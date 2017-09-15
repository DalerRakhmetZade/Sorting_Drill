def Sort(list1,list2):
    for i in range(1,len(list1)):
        currentvalue = list1[i]
        position = i
        while position>0 and list1[position-1]>currentvalue:
            list1[position]=list1[position-1]
            position=position - 1
        list1[position]=currentvalue
        
    for i in range(1,len(list2)):
        currentvalue = list2[i]
        position = i
        while position>0 and list2[position-1]>currentvalue:
            list2[position]=list2[position-1]
            position=position - 1
        list2[position]=currentvalue
        
list1 = [67, 45, 2, 13, 1, 998]
list2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
Sort(list1, list2)
print(list1, list2)
