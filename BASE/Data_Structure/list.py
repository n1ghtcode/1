# data structure
# list
import os, time

os.system('color a')

word = 'python'
list = [1, 2, 3, 4, 5]
wrd_lst = [char for char in word] #Создал список через генератор списка.
#slice срез по нашему    list[start:stop:step]
re_pyt = wrd_lst[::-1] # reverse list
print(re_pyt)

#############################################
time.sleep(5)
os.system('cls')
os.system('color 4')
#############################################
nums = [1, 222, 2, 222, 3, 222]
nums2 = [222, 5, 222, 6, 222, 7]

nums.remove(222)
nums.insert(1, 111)
nums.append(4)
nums.extend(nums2)
unwanted = nums.pop(1)
#print(nums.index(7))
count_nums = nums.count(222)
#print(count_nums)
nums.sort()
nums.reverse()
#wrd_lst.reverse()
print(wrd_lst)

print(nums)

time.sleep(5)
nums.extend(wrd_lst)

cpy_list = nums.copy()
##############################################
os.system('cls')

nums.clear()
print(nums)
time.sleep(3)

print(cpy_list * 100)
time.sleep(3)

