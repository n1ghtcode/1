import time

names = ['alice', 'frank', 'kasha']
numbers = [x for x in range(0, 11, 2)]
names = [name.upper() for name in names]
names.pop(2)
numbers.pop(0)

print(names)
print(numbers)

time.sleep(4)