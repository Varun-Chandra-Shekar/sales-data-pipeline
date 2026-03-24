# src/utils.py
# Generating sample sales data for our pipeline

# A single sale as a dictionary — key:value pairs
sale = {
    "order_id": 1,
    "product": "Laptop",
    "quantity": 2,
    "price": 999.99,
    "customer": "Alice Johnson",
    "status": "paid"
}

# Access values using keys
print(f"Order #{sale['order_id']}: {sale['customer']} bought {sale['quantity']}x {sale['product']}")
print(f"Total: ${sale['price'] * sale['quantity']}")

# A list of sales — this is what real data looks like
sales = [
    {"order_id": 1, "product": "Laptop",     "quantity": 2, "price": 999.99, "customer": "Alice Johnson",  "status": "paid"},
    {"order_id": 2, "product": "Mouse",       "quantity": 5, "price": 24.99,  "customer": "Bob Smith",      "status": "pending"},
    {"order_id": 3, "product": "Keyboard",    "quantity": 1, "price": 74.50,  "customer": "Charlie Brown",  "status": "paid"},
    {"order_id": 4, "product": "Monitor",     "quantity": 1, "price": 349.00, "customer": "Alice Johnson",  "status": "overdue"},
    {"order_id": 5, "product": "Laptop",      "quantity": 1, "price": 999.99, "customer": "Diana Prince",   "status": "paid"},
    {"order_id": 6, "product": "Mouse",       "quantity": 3, "price": 24.99,  "customer": "Bob Smith",      "status": "paid"},
    {"order_id": 7, "product": "Headphones",  "quantity": 2, "price": 59.99,  "customer": "Eve Wilson",     "status": "pending"},
    {"order_id": 8, "product": "Laptop",      "quantity": 1, "price": 999.99, "customer": "",               "status": "paid"},
    {"order_id": 9, "product": "keyboard",    "quantity": 1, "price": -10.00, "customer": "Frank Miller",   "status": "paid"},
    {"order_id": 10, "product": "Monitor",    "quantity": 0, "price": 349.00, "customer": "Grace Lee",      "status": "unknown"},
]

# Loop through and print each sale
print(f"\nTotal orders: {len(sales)}\n")

for sale in sales:
    total = sale["price"] * sale["quantity"]
    print(f"Order {sale['order_id']}: {sale['customer']} — {sale['product']} — ${total:.2f} — {sale['status']}")s