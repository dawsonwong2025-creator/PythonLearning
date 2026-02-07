


values = [1,5,-7,6,7,8,9,-10,11,24,-23452,5423523]
maxvalue = values[0]
for i in range(1,len(values)):
    print(i, values[i], maxvalue, values[i] > maxvalue)
    if values[i] > maxvalue:
        maxvalue = values[i]
    
print(maxvalue)
    

