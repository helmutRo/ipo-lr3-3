print ("Введите день - ", end = " ")
a = int(input()) #Запрашивается день
print ("Введите месяц - ", end = " ")
b = int(input()) #Запрашивается месяц
if b == 12 or b == 1 or b == 2: #зимние месяцы
    print(f"{a} {b} - зима")
elif b < 6: #весенние месяцы
    print(f"{a} {b} - весна")
elif b < 9: #летние месяцы
    print(f"{a} {b} - лето")
else: #осенние месяцы
    print(f"{a} {b} - осень")