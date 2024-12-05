# Даны два списка:first и second
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

#  Генераторная сборка first_result:   - zip(first, second): объединяет элементы из двух списков попарно.
#  Например, ('Strings', 'Строка'), ('Student', 'Урбан'), ('Computers', 'Компьютер').
#  for x, y in zip(...): перебирает пары строк x из first и y из second.
#  if len(x) != len(y): проверка, разные ли длины строк.
#  len(x) - len(y): вычисляет абсолютное значение разницы в длине строк, если они не равны.

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))

#  Генераторная сборка second_result:range(len(first)): создает последовательность индексов от 0 до длины списка first.
#  len(first[i]) == len(second[i]): сравнивает длины строк по соответствующим индексам в списках first и second.
#  Если длины равны, возвращает True, в противном случае False.

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
