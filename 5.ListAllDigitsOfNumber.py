n = 123456789012345
r = n % 10
print(r)
a = int((n-r)/10)%10
print(a)
b = int((n-a/10))%10-1
print(b)
c = int((n-b/10))%10-2
print(c)
d = int((n-c/10))%10-3
print(d)
e = int((n-d)/10)%10-4
print(e)
f = int((n-e/10))%10-5
print(f)
g = int((n-f/10))%10-6
print(g)
h = int((n-g/10))%10-7
print(h) 
i = int((n-h/10))%10-8
print(i)
j = int((n-i/10))%10-9
print(j)
k = int((n-j/10))%10-10
print(k)
l = int((n-k)/10)%10-11
print(l)
m = int((n-l/10))%10-12
print(m)
n = int((n-m/10))%10-13
print(n)
o = int((n-n/10))%10-14
print(o) 

