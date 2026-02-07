def findMin(values):
    minvalue = values[0]
    for i in range(1,len(values)):
        #print(i, values[i], minvalue, values[i] > minvalue)
        if values[i] < minvalue:
            minvalue = values[i]

    return minvalue





values = [1,5,-7,6,7,8,9,-10,11,24,-23452,5423523]
a = findMin(values)
print("result 1:",a)
print("result 2:",findMin([-1, 1,2,-4]))
    

