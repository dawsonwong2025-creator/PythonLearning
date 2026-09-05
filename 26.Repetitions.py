# dna = "AAGGGGGCAGAATTA"
dna = input("Please input your dna here-->")
count = 1
high = 0
if len(dna) > 1:
    for j in range(1,len(dna)):
        i = j-1
        if dna[j] == dna[i]:
            count = count + 1
            
            if high < count:
                high = count
            
        else:
            count = 1
    

elif len(dna) == 1:
    high = 1
else:
    high = 0
    


print(high)

            


