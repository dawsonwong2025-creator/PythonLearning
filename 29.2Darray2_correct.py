array = [
    [-100,-2,-3,-4],
    [5,6,7],
    [8,9],
]


result = []

for r in range(len(array)):
    rmmbr = array[r][0]
    for c in range(len(array[r])):
        if rmmbr > array[r][c]:
            rmmbr = array[r][c]
    print(rmmbr)

    result.append(rmmbr)

print(result)