def sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def bubbleSort(list):
    bubble = None
    while not(sorted(list)):
        print list
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                bubble = list[i+1]
                list[i+1] = list[i]
                list[i] = bubble
    return list


print bubbleSort([9,8,7,6,5,4,3,2,1])
