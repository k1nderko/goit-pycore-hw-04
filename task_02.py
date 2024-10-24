def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_list.append(cat_info)
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    
    return cats_list
cats_info = get_cats_info("D:\Python\goit-pycore-hw-04\sal.txt")
print(cats_info)