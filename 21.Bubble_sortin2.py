number_list = [2, 8, 1, -2]
for i in range(0,len(number_list)):
    for j in range(i+1,len(number_list)):
          if number_list[j]<number_list[i]:
            it = number_list[j]
            number_list[j] = number_list[i]
            number_list[i] = it
print(number_list)