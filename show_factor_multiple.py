n = 10

for i in range(1, n+1):
    if n % i == 0 :
        # as n / i will convert to type from int to float, 
        # use int() function to convert back to int, let it shows pretty
        j = int(n / i)
        print(n, ' = ', i, ' * ', j)