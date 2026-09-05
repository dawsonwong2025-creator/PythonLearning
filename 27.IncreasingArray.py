# input
f = open('data.txt', 'r')
firstline = f.readline()
n = int(firstline)
secondline = f.readline()
fields = secondline.split(' ')
numbers = []
for i in range(n):
    numbers.append(int(fields[i]))
f.close()

# work (n, numbers)
count = 0
for j in range(1,len(numbers)):
    p = j - 1
    if j < p:
        count = count + 1
        numbers[j] = numbers[j] + 1


print(count)

# print result
# 5

