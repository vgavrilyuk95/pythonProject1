my_list = [1,2,3,4,5,6,7,8,9,10]
a = int(input('Оцените от 1 до 10: '))
b = my_list.count(a)
for element in my_list:
    if b > 0:
        i = my_list.index(a)
        my_list.insert(i+b, a)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, a)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(a)
print(my_list)