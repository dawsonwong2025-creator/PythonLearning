#input 5
# 3 2 1 5 
#output 5
sum_of_n = 0
sum_of_others = 0
n = int(input("totalnum:"))
sum_of_n = int(n*(n+1)/2)

print(sum_of_n)
for i in range(n-1):
    some = int(input("Other nums:"))
    
    sum_of_others = sum_of_others + some
missing_num = sum_of_n - sum_of_others

print(missing_num)
    