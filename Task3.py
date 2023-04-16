# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.




n = int(input("Введите число: "))


i = 1
result = 1
while i:
    result1 = result
    result = result*2
    i +=1
    print(result1)
    if result > n:

        break






