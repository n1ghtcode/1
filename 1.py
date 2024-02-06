num = input('Числа через пробел: ')
num_list = [int(i) for i in num.split()]
num_list.append(3)
num_list.pop(0)
print(num_list)