# Запрос размеров комнаты
length = float(input("Введите длину комнаты (в метрах): "))
width = float(input("Введите ширину комнаты (в метрах): "))
height = float(input("Введите высоту комнаты (в метрах): "))

# Вычисление объема комнаты
volume = length * width * height

# Определение типа комнаты
room_type = ""
if volume < 30:
    room_type = "маленькая"
elif volume >= 30 and volume < 60:
    room_type = "средняя"
else:
    room_type = "большая"

# Вывод результата
print(f"Объем комнаты: {volume} кубических метров")
print(f"Это {room_type} комната.")

# Запрос длины последовательности Фибоначчи
n = int(input("Введите длину последовательности Фибоначчи: "))

# Инициализация первых двух чисел Фибоначчи
a, b = 0, 1

# Вывод первых n чисел Фибоначчи
fibonacci_sequence = [a, b]
while len(fibonacci_sequence) < n:
    a, b = b, a + b
    fibonacci_sequence.append(b)

print(f"Последовательность Фибоначчи: {fibonacci_sequence}")

# Запрос длины последовательности Фибоначчи
n = int(input("Введите длину последовательности Фибоначчи: "))

# Инициализация первых двух чисел Фибоначчи
a, b = 0, 1

# Создание списка для хранения чисел Фибоначчи
fibonacci_sequence = [a, b]

# Генерация и добавление чисел Фибоначчи в список
while len(fibonacci_sequence) < n:
    a, b = b, a + b
    fibonacci_sequence.append(b)

print(f"Последовательность Фибоначчи: {fibonacci_sequence}")

# Запрос длины последовательности Фибоначчи
n = int(input("Введите длину последовательности Фибоначчи: "))

# Инициализация первых двух чисел Фибоначчи
a, b = 0, 1

# Создание списка для хранения чисел Фибоначчи
fibonacci_sequence = [a, b]

# Генерация и добавление чисел Фибоначчи в список
while len(fibonacci_sequence) < n:
    a, b = b, a + b
    fibonacci_sequence.append(b)

print(f"Последовательность Фибоначчи: {fibonacci_sequence}")

# Подсчет четных и нечетных чисел
even_count = 0
odd_count = 0

for num in fibonacci_sequence:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

total_numbers = even_count + odd_count

# Вывод результатов
print(f"Количество четных чисел: {even_count}")
print(f"Количество нечетных чисел: {odd_count}")
print(f"Процент четных чисел: {(even_count / total_numbers) * 100}%")
print(f"Процент нечетных чисел: {(odd_count / total_numbers) * 100}%")
