my_list = list()
for i in range(1,5050505,23):
     my_list.append(i)

total = 0

for i in range(0, len(my_list)):
    total = total + my_list[i]
    print(total)


