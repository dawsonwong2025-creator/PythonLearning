n = 4
for i in range(0, n):
    numOfStars = i+1
    numOfSpaces = n - numOfStars

    stars = ""
    for p in range(1, numOfStars+1):
        stars = stars + '*'

    spaces = ""
    for p in range(1, numOfSpaces+1):
        spaces = spaces + ' '
    print(spaces+stars)