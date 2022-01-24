oborot = float(input("Введите выручку фирмы "))
zatrati = float(input("Введите издержки фирмы "))
if oborot > zatrati:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {oborot / zatrati:.2f}")
    sotr = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {oborot / sotr:.2f}")
elif oborot == zatrati:
    print("Фирма работает в ноль")
else:
    print("Пора закрывать фирму")