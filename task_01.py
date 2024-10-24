def total_salary(path):
    try:
        total = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        average = total / count if count else 0
        return total, average

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("D:\Python\goit-pycore-hw-04\sal.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")