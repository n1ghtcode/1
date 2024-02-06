#сумма всех чисел кратных трём и пяти до 1000
import time, os

os.system('color b')
os.system('cls')

a = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
a = sum(a)
print(a)

time.sleep(3)