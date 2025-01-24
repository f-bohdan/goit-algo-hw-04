def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as info_file:
            # створюємо пустий список "котів"
            cats = []
            for line in info_file.readlines():
                try:
                    characteristics = {}
                    # отримуємо дані з рядка та вносимо в словник
                    characteristics["id"], characteristics["name"], characteristics["age"] = line.strip().split(',')
                    # додаємо "котика" до списку
                    cats.append(characteristics)
                except ValueError:
                    print("Файл не відповідає вимогам")
                    return None
            if not cats:
                print("Файл пустий")
                return None
            # в кінцевому результаті повертаємо список
            return cats
            
    except FileNotFoundError:
        print("Файл не знайдено")

print(get_cats_info("cats_file.txt"))