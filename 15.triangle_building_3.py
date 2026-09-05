n = 4
stars = ""

for i in range(0, n):
    numOfStars = i+1
    numOfSpaces = n - numOfStars

    stars = stars + '*'

    spaces = ""
    for p in range(1, numOfSpaces+1):
        spaces = spaces + ' '
    print(spaces+stars)