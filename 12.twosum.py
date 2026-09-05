nums = [2,7,11,18]
target = 9
a= 0
b= 0
n= 0
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(nums[i], '+', nums[j], '=', nums[i]+nums[j])
            #either is okay!
            #print(a, "+", b, "=", n)
            a=nums[i]
            b=nums[j]
            n=nums[i]+nums[j]





#print(answer) 2+7=9