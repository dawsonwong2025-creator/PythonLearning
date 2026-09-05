def printstars(n, i):
    numOfStars = 1+2*i
    numOfSpaces = n - numOfStars +i

    stars = ""
    for p in range(1, numOfStars+1):
        stars = stars + '*'

    spaces = ""
    for p in range(1, numOfSpaces+1):
        spaces = spaces + ' '
    print(spaces+stars+spaces) 

n = input("num:") 
n = int(n)
for i in range(0, n):
    printstars(n, i)

for j in range (1,n):
    k = (n - 1) - j
    printstars(n, k)
