r=input("number:")
r = int(r)
t=r%10
n=int((r%100-t)/10)
g=int((r%1000-(r%100))/100)
print(((( t + n + g))))

