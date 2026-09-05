#input numbers
#input until input 0 to stop
#output all the nums except for zero
nums = int(input())

dfs = 0


while nums != 0:
    dfs = dfs + 1 
    nums = int(input())
    #print(nums)
    
print("You input",dfs,"numbers.")
print("See you next time, bye!")
