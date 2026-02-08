it = [3, 2, 8, 4]

print(it)
for i in range(0,len(it)):
    for j in range(i+1,len(it)):
        if it[i]>it[j]:
            something = it[i]
            it[i] = it[j]
            it[j] = something
            print(it, i, "<->", j)
    
    
print(it)