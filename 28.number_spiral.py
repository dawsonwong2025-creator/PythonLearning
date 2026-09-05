f = open('data.2.txt', 'r')

firstline = f.readline()
n = int(firstline)

numbers = []
hm = 0
um = 0

for i in range(n):
    otherline = f.readline()
    otherfields = otherline.split()

    row = int(otherfields[0])
    column = int(otherfields[1])
    some = [row, column]

    numbers.append(some)
    print(numbers[i])
    if row>column:
        #print(row)
        hm = (row*row-(row-1))
        #print(hm)
        um = row-column
        #print(um)
        if row % 2 == 0:
            ym = hm + um
        else:
            ym = hm - um
        print(ym)

    elif row<column:
        #print(column)
        hm = (column*column-(column-1))
        #print(hm)
        um = column-row
        #print(um)
        if column % 2 == 0:
            ym = hm - um
        else:
            ym = hm + um
        print(ym)

    else:
        hm = (row*row-(row-1))
        print(hm)
f.close()

    