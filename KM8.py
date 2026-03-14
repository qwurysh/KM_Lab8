import requests
import random

def get_random_post():
    # 1. Створюємо власний генератор випадкових чисел від 1 до 100
    # 2-3. Отримуємо випадкове айді та зберігаємо його у змінну
    random_id = random.randint(1, 100)
    
    # 4. Змінна робить API динамічним (підставляємо random_id у посилання)
    url = f"https://jsonplaceholder.typicode.com/posts/{random_id}"
    
    try:
        # Відправляємо GET-запит до нашого API
        response = requests.get(url)
        response.raise_for_status() 
        
        # 5. Парсимо отриманий JSON-файл у Python-об'єкт (словник)
        post_data = response.json()
        
        # 6. Виводимо дані з об'єкта в консоль (айді, титул і тіло)
        print(f"--- Результат для ID: {post_data.get('id')} ---")
        print(f"Титул (Title): {post_data.get('title')}")
        print("-" * 30)
        print(f"Тіло (Body):\n{post_data.get('body')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка під час виконання запиту: {e}")

if __name__ == "__main__":
    get_random_post()
