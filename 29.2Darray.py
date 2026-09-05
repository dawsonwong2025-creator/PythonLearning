array = [
    [12, 13,-2,-3],
    [2,3,-1]
]

total = 0

# for row in array:
#     print(row)
#     for number in row:
#         total = total + number

for i in range(0, len(array)):
    print('i = ',i, array[i])
    for j in range(0, len(array[i])):
        print('.    j =',j)
        total = total + array[i][j]

print("Total:", total)

