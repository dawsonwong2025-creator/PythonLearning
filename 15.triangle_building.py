#n = 5
#m = n*" "
#for i in range(0,n):
    #b = m + "*"
    #n = n - 1
    #print(b)
n = 3
e = " " + ""
for i in range(0,n):
    m = str((n-(n-1))*"*")
    e = e + m + "*" 
    print(e)