import requests
import json
import time

def save_empty_items():
    try:
        response = requests.get('http://localhost:8000/items')
        if response.status_code == 200:
            items = response.json()
            empty_items = [item for item in items if item['quantity'] == 0]
            filename = f"empty_items_{time.strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(empty_items, f)
            print(f"Empty items saved to {filename}")
        else:
            print(f"Failed to fetch items. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Calling the API every 1 minute
while True:
    save_empty_items()
    time.sleep(60)
