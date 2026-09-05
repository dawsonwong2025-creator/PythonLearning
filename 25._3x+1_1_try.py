#input n
#if n is even, divide by 2
#if n is odd multiply 3 add 1
#until num = 1
n = int(input("The starting number:"))
the_list=[]
while n != 1:
    print(n)
    the_list.append(n) 
    if n % 2 == 0:
        # even
        n=int(n/2)
    else:
        n = 3 * n + 1


print(n)
the_list.append(n) 
answer = ' '.join(map(str,the_list))
print(the_list)
print(answer)
