num = int(input())
list = []

# input a new number
newnum = int(input("Num1:"))
list.append(num)
list.append(newnum)
newnum1 = int(input("Num2:"))
list.append(newnum1)
newnum2 = int(input("Num3:"))
list.append(newnum2)
newnum3 = int(input("Num4:"))
list.append(newnum3)
newnum4 = int(input("Num5:"))
list.append(newnum4)

i = len(list)-1
while (i-1>=0 and list[i-1]>list[i]):
    cup = list[i-1]
    list[i-1] =list[i]
    list[i] = cup
    i-=1


print(list)
