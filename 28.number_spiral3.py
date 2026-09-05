def max(i,j):
    if i>j:
        return i
    else:
        return j

    
def work(otherline):
    otherfields = otherline.split()
    
    row = int(otherfields[0])
    column = int(otherfields[1])

    k = max(row, column)
    s = 0
    if k % 2 == 0:
        s = 1
    else: 
        s = -1

    return (k-1)*(k-1)+k+s*(row-k)-s*(column-k)

    

f = open('data.3.txt', 'r')

firstline = f.readline()
n = int(firstline)

numbers = []
hm = 0
um = 0

for i in range(n):
    otherline = f.readline()
    answer = work(otherline)
    print(answer)
    
f.close()


