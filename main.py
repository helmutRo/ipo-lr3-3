print("Введите день: ", end = "")
day = int(input()) #запрашивается день
print("Введите месяц: ", end = "")
mon = int(input()) #запрашивается месяц
if(mon < 0 or day < 0):
    print("Неверная дата")
elif (mon == 1 and day < 32) or (mon == 2 and day < 30) or (mon == 12 and day < 32):  #зимние месяцеы
    print(f"{day}.{mon} - Зима")
elif (mon == 3 and day < 32) or (mon == 4 and day < 31) or (mon == 5 and day < 32): #весенние месяцеы
    print(f"{day}.{mon} - Весна")
elif (mon == 6 and day < 31) or (mon == 7 and day < 32) or (mon == 8 and day < 32): #летние месяцеы
    print(f"{day}.{mon} - Лето")    
elif (mon == 9 and day < 31) or (mon == 10 and day < 32) or (mon == 11 and day < 31): #осенние месяцеы
    print(f"{day}.{mon} - Осень")
else:
    print("Неверная дата")
