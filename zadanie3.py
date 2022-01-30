my_list = ['Зима', 'Весна', 'Лето', 'Осень']
my_dict = {0: 'Зима', 1: 'Весна', 3: 'Лето', 4: 'Осень'}
a = int(input("Введите числом месяц "))
if a == 12 or a == 1 or a == 2:
    print(my_list[0])
elif a == 3 or a == 4 or a == 5:
    print(my_list[1])
elif a == 6 and a == 7 and a == 8:
    print(my_list[2])
elif a == 9 or a == 10 or a == 11:
    print(my_list[3])
else:
    print("Это за пределами нашего сознания")
