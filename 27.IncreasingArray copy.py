f = open('data.txt', 'r')
firstline = f.readline()
n = int(firstline)
secondline = f.readline()
fields = secondline.split(' ')
numbers = []
for i in range(n):
    numbers.append(int(fields[i]))
f.close()

moves = 0
for i in range(1, n):
    if numbers[i] < numbers[i - 1]:
        moves += numbers[i - 1] - numbers[i]
        numbers[i] = numbers[i - 1]
print(firstline)
print(secondline)
print(moves)

