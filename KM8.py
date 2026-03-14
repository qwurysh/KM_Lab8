import requests
import random

def get_random_post():
    # 1. Створюємо власний генератор випадкових чисел від 1 до 100
    # 2. Зберігаємо згенероване айді у змінну
    random_id = random.randint(1, 100)
    
    # 3. Робимо API динамічним за допомогою f-рядка та змінної random_id
    url = f"https://jsonplaceholder.typicode.com/posts/{random_id}"
    
    try:
        # Робимо GET-запит до API
        response = requests.get(url)
        response.raise_for_status()  # Перевірка на успішність запиту (код 200)
        
        # 4. Парсимо отриманий JSON-файл у Python-об'єкт (словник)
        post_data = response.json()
        
        # 5. Виводимо номер айді, титул і тіло в консоль
        print(f"--- Результат для ID: {post_data.get('id')} ---")
        print(f"Титул (Title): {post_data.get('title')}")
        print("-" * 30)
        print(f"Тіло (Body):\n{post_data.get('body')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка під час виконання запиту: {e}")

if __name__ == "__main__":
    get_random_post()
