# Sports Equipment Inventory System

This project implements a sports equipment inventory system using Django, with RESTful APIs for creating, updating, and retrieving items. Additionally, a script is provided to fetch items with no quantity left every 1 minute and save them to a JSON file.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/sports-equipment-inventory.git
    cd sports_equipment_inventory/Sports_Equipment_Inventory
    ```

2. **Install dependencies:**

    Ensure you have Python and Django installed on your system. You can install Django using pip.

    ```bash
    pip install django
    ```

3. **Run migrations:**

    Migrate the database to create the required tables.

    ```bash
    python manage.py migrate
    ```

## Running the Django Server

To run the Django development server:

```bash
python manage.py runserver
```


### The server will start running at http://localhost:8000.

Using the APIs
Create Item
Endpoint: `POST /items`


Example request body:
```json
{
  "name": "Football",
  "quantity": 10
}
```

Update Item Quantity
Endpoint: `PATCH /items/<equipment_id>`

Example request body:
```json
{
  "quantity": 15
}
```

Get Items
Endpoint: `GET /items`


## Running the Script
To run the script to fetch items with no quantity left and save them to a JSON file:

```bash
python inventory_script.py
```

The script will run indefinitely, fetching empty items every 1 minute and saving them to a new JSON file.

✌️✌️
