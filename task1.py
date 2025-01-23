def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as info_file:
            # стартові значення
            quanitty_workers = 0
            sum_sallary = 0
            for line in info_file.readlines():
                # отримуємо з рядка значення зарплати
                try:
                    _, value = line.split(',')
                    # розразовуємо суму
                    sum_sallary += int(value)
                    quanitty_workers += 1
                except ValueError:
                    print("Введено не вірне значення зарплати")
                    return None
            # повертаємо суму і середню зарплату
            if not quanitty_workers:
                print("Файл пустий")
                return None
            return sum_sallary, int(sum_sallary/quanitty_workers)
            
    except FileNotFoundError:
        print("Файл не знайдено")

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
