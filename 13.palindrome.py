x = "123"

a = x[0]
b = x[1]
c = x[2] 
print(a)
d = a
a = c
b = b
c = d

print(a,b,c,c,b,a)

# lenX = 6
#i = 0 1 2 3 4 5
#j = 5 4 3 2 1 0
#j = lenX-1-i

x = "`aba`"
y = ""
for i in range(0, len(x)):
    print(i)
