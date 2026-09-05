def sumOfAllEvenNumber(list):
    d = 0
    for i in range(len(a)):
        if a[i] % 2 == 1:
            d += a[i]
    return d 

a = [3,7,2,9, 1, 0,4]
b = sumOfAllEvenNumber(a)
print(b) # 6