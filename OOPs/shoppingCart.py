class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price, quantity=1):
        if item in self.cart:
            self.cart[item]['quantity'] += quantity
        else:
            self.cart[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.cart:
            self.cart[item]['quantity'] -= quantity
            if self.cart[item]['quantity'] <= 0:
                del self.cart[item]

    def get_cart_items(self):
        return list(self.cart.keys())

    def get_total_items(self):
        return sum(item_info['quantity'] for item_info in self.cart.values())

    def get_total_price(self):
        return sum(item_info['price'] * item_info['quantity'] for item_info in self.cart.values())

cart = ShoppingCart()

cart.add_item("Apple", 2.5, 3)
cart.add_item("Banana", 1.0)
cart.add_item("Orange", 1.5, 2)

print("Items in the cart:", cart.get_cart_items())
print("Total items in the cart:", cart.get_total_items())

print("Total price of items in the cart:", cart.get_total_price())

cart.remove_item("Apple", 2)
cart.remove_item("Banana")

print("Updated items in the cart:", cart.get_cart_items())
print("Updated total items in the cart:", cart.get_total_items())

print("Updated total price of items in the cart:", cart.get_total_price())
