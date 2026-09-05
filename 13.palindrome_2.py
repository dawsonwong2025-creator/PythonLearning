x = "jkhg"
n= len(x)
e=""
for i in range(0, len(x)):
    k = n-1-i
    m = x[k]
    #e = m
    e = e + m

checkResult = (e==x)
print(checkResult)     