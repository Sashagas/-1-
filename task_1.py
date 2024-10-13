numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# Находим индекс пропущенного элемента
missing_index = numbers.index(None)

# Суммируем все элементы, кроме пропущенного
total_sum = sum(numbers[:missing_index] + numbers[missing_index+1:])

# Рассчитываем среднее арифметическое
average = total_sum / len(numbers)

# Заменяем пропущенный элемент средним
numbers[missing_index] = average

print(numbers)


