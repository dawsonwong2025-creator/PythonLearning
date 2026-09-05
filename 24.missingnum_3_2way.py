#input 5
# 3 2 1 5 
#output 5
sum_of_n = 0
sum_of_others = 0
n = int(input("totalnum:"))
for p in range(n):
    sum_of_n = sum_of_n + (p+1)

for i in range(n-1):
    some = int(input("Other nums:"))
    
    sum_of_others = sum_of_others + some
missing_num = sum_of_n - sum_of_others
print(missing_num)
    