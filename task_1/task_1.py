
# Задание 1

# Функция алгоритма, в зависимости от поданных данных выстраивает машины в ряд,
# если разность >= 1 то с помощью цикла while уравниваем их количество добавляя в ряд 2 машины которых больше и 1 машину которых меньше
# после того как количесвто машин уравняется вымтраиваем их просто друг за другом
def algoritm(red_car, wait_car, type):
    while red_car != 0:
        if type == 'R':
            if red_car != wait_car:
                result.append('WRR')
                red_car = red_car - 2
                wait_car = wait_car - 1
            else:
                result.append('WR')
                red_car = red_car - 1
                wait_car = wait_car -1
        else:
            if red_car != wait_car:
                result.append('RWW')
                red_car = red_car - 1
                wait_car = wait_car - 2
            else:
                result.append('RW')
                red_car = red_car - 1
                wait_car = wait_car -1

print('Введите количество красных машин')
red_car = input()

print('Введите количество белых машин')
wait_car= input()

result = []

# Проверка на пограничные условия, что данные являются цифрами,
# количество определенных машин не равно 0 и разность машин не больше 2
try:
    red_car = int(red_car)
    wait_car = int(wait_car)

except Exception:
    print('Некорректные данные')
    exit()

if  red_car == 0 or wait_car == 0 or red_car / wait_car > 2 or wait_car/ red_car > 2:
    print('Нет решения')
    exit()

# Проверка на равность или неравность количества машин
# В первом случае красных машин больше, во втором белых, в третьем их одинаковое количество, и прогоняем их через функцию алгоритма,
if red_car > wait_car:
    result.append('R')
    red_car = red_car - 1
    algoritm(red_car, wait_car, 'R')

elif wait_car > red_car:
    result.append('W')
    wait_car = wait_car - 1
    algoritm(red_car, wait_car, 'W')

else:
    algoritm(red_car, wait_car, 'R')
    
[print(res, end='') for res in result]
