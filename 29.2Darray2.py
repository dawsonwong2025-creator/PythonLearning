array = [
    [-100,-2,-3,-4],
    [5,6,7],
    [8,9],
]


result = []

for r in range(len(array)):
    rmmbr = 0
    for c in range(len(array[r])-1):
        if array[r][c]>=array[r][c+1]:
            if rmmbr <array[r][c]:
                rmmbr = array[r][c]

        else:
            if rmmbr <array[r][c+1]:
                rmmbr = array[r][c+1]
    print(rmmbr)

    result.append(rmmbr)

print(result)