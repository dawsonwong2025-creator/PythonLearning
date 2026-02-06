#r=input("number:")
#r = int(r)
sum = 0
equation = ""
r=1234


while r>0:
    t=r%10
    r=int(r/10)
    sum = sum + t
    if equation=="":
        equation = str(t)
    else:
        equation = str(t) + "+" + equation

print(equation,'=', sum)

#n=int((r%100-t)/10)
#g=int((r%1000-(r%100))/100)
#print(((( t + n + g))))

