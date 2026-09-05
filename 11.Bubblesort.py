#.     i=1 
#.         j=2
it =[0,10,23,1,3]

for i in range(0,len(it)):
    for j in range(i+1,len(it)):
        if it[j]<it[i]:
            cup = it[j]
            it[j] = it[i]
            it[i] = cup
            
print(it)           
            

