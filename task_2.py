# Параметры книги
pages = 100
rows_per_page = 50
symbols_per_row = 25

# Параметры дискеты
disk_size = 1.44  # Мб
bytes_per_symbol = 4  # байт

# Расчет размера одной книги в байтах
book_size = pages * rows_per_page * symbols_per_row * bytes_per_symbol

# Преобразование размера дискеты в байты
disk_size_bytes = disk_size * 1024 * 1024

# Расчет количества книг
book_count = disk_size_bytes // book_size

# Вывод результата
print(f"На дискету можно поместить {book_count} книг.")


