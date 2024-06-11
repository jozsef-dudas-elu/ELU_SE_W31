def calculate_total(cart):
    total = 0
    for item in cart:
        total += float(item['price'])
    return total


def display_total(Total):
    print("Total price: " + str(Total))


CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': '8.49'}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

if __name__ == '__main__':
    shopping_cart_total = calculate_total(CART)
    display_total(shopping_cart_total)
