#input 5
# 3 2 1 5 
#output 5
sum_of_n = 0
sum_of_others = 0
n = int(input("totalnum:"))

a = [0] * (n+1)

for i in range(n-1):
    some = int(input("Other nums:"))
    a[some] = 1
print(a)
answer = 0
for i in range(1,n+1):
    if (a[i]==0):
        answer = i
# missing_num = sum_of_n - sum_of_others
print(answer)
    