import requests
import csv

def fetch_api_data():
    # Используем надежный публичный API со списком дел
    url = "https://jsonplaceholder.typicode.com/todos"
    print(f"Connecting to {url}...")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Проверка на ошибки
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def process_and_save(data):
    if not data:
        print("No data to save.")
        return

    # Определяем заголовки таблицы на основе ключей JSON
    fields = data[0].keys()
    filename = "api_export_results.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Success! Saved {len(data)} rows to {filename}")

if __name__ == "__main__":
    raw_data = fetch_api_data()
    process_and_save(raw_data)
