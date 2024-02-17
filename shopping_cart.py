"""
Added creativity: Enhanced display formatting for better readability and included quantity information for each item in the shopping cart.
"""

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.prices = []
        self.quantities = []

    def add_item(self, name, price, quantity=1):
        self.items.append(name)
        self.prices.append(price)
        self.quantities.append(quantity)
        print(f"Added {quantity} '{name}' to the cart at ${price:.2f} each.")

    def display_cart(self):
        print("\nThe contents of the shopping cart are:")
        print(f"{'Item':<15} {'Quantity':<10} {'Price':<10}")
        for i, item in enumerate(self.items, start=1):
            quantity = self.quantities[i - 1]
            price = self.prices[i - 1]
            total_price = quantity * price
            print(f"{i}. {item:<15} {quantity:<10} ${price:.2f} ({total_price:.2f})")

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
            del self.prices[index]
            del self.quantities[index]
            print("Item removed.")
        else:
            print("Invalid index. Please choose a valid item number.")

    def compute_total(self):
        total = sum(quantity * price for quantity, price in zip(self.quantities, self.prices))
        return f"\nThe total price of the items in the shopping cart is ${total:.2f}"

# Example usage:
print("Welcome to the Enhanced Shopping Cart Program!")

shopping_cart = ShoppingCart()

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = input("Please enter an action: ")

    if action == "1":
        item_name = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of '{item_name}'? "))
        item_quantity = int(input(f"How many '{item_name}' would you like to add? ") or 1)
        shopping_cart.add_item(item_name, item_price, item_quantity)
    elif action == "2":
        shopping_cart.display_cart()
    elif action == "3":
        index = int(input("Which item would you like to remove? ")) - 1
        shopping_cart.remove_item(index)
    elif action == "4":
        print(shopping_cart.compute_total())
    elif action == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

