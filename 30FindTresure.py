def readMapFromFile():
    f = open('map.txt', 'r')

    firstline = f.readline()
    nums = firstline.split()
    row = int(nums[0])
    col = int(nums[1])

    map = []
    for i in range(row):
        maprow = f.readline()
        map.append(maprow.split())
    f.close()
    return row, col, map

def findLocationOfRobot(row, col, map):
    for r in range(row):
        for c in range(col):
            if map[r][c]=='R':
                return r, c
    return -1, -1

def didVisitBefore(tryWalkingRow, tryWalkingCol, breadcrumbs):
    for i in range(len(breadcrumbs)):
        if breadcrumbs[i][0]==tryWalkingRow and breadcrumbs[i][1]==tryWalkingCol:
            return True
    return False


mapRow, mapCol, map = readMapFromFile()
robotRow, robotCol  = findLocationOfRobot(mapRow, mapCol, map)

# ==================================
# finding the treasure
# ==================================
breadcrumbs = [
    [robotRow, robotCol, 'NONE', -1]
]

DIRECTIONS = [
    [-1, 0, '↑'], #UP
    [0, 1, '→'], #RIGHT
    [1, 0, '↓'], #DOWN
    [0, -1, '←'], #LEFT
]

isSuccessToFindTresure = False
stepNum = 0
while (not isSuccessToFindTresure and stepNum <= len(breadcrumbs)):
    walkingRow = breadcrumbs[stepNum][0]
    walkingCol = breadcrumbs[stepNum][1]
    for d in range(len(DIRECTIONS)):
        if not isSuccessToFindTresure:
            tryWalkToRow = walkingRow+DIRECTIONS[d][0]
            tryWalkToCol = walkingCol+DIRECTIONS[d][1]
            if tryWalkToRow>=0 and tryWalkToRow<mapRow and \
                tryWalkToCol>=0 and tryWalkToCol<mapCol and \
                (map[tryWalkToRow][tryWalkToCol]=='0' or map[tryWalkToRow][tryWalkToCol]=='*') and \
                not didVisitBefore(tryWalkToRow, tryWalkToCol, breadcrumbs):

                breadcrumbs.append([tryWalkToRow, tryWalkToCol, d, stepNum])
                if map[tryWalkToRow][tryWalkToCol]=='*':
                    isSuccessToFindTresure = True
    stepNum+=1

# ==================================
# construct the walking path
# ==================================
indexOfStep = len(breadcrumbs)-1
while (indexOfStep>0):
    step = breadcrumbs[indexOfStep]

    directionChar = step[2]
    beforeIndexOfStep = step[3]
    
    beforeStep = breadcrumbs[beforeIndexOfStep]
    beforeWalkingRow = beforeStep[0]
    beforeWalkingCol = beforeStep[1]
    map[beforeWalkingRow][beforeWalkingCol]=DIRECTIONS[directionChar][2]
    indexOfStep = beforeIndexOfStep


# ==================================
# show the result
# ==================================
for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c]=='0':
            map[r][c]=' '
        elif map[r][c]=='1':
            map[r][c]='■'
        elif map[r][c]=='*':
            map[r][c]='$'


for r in range(len(map)):
    print(' '.join(map[r]))