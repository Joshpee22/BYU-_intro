# Get user input
child_meal_price = float(input("Enter the price of a child's meal: "))                                                adult_meal_price = float(input("Enter the price of an adult's meal: "))                                               num_children = int(input("Enter the number of children: "))num_adults = int(input("Enter the number of adults: "))                                                               # subtotal                                                 subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# sales tax rate
sales_tax_rate = float(input("Enter the sales tax rate (percentage): "))

# Calculate sales tax
sales_tax = (subtotal * sales_tax_rate) / 100

# Calculate total price
total_price = subtotal + sales_tax

# Display sales tax and total price
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total Price: ${total_price:.2f}')

# Ask for payment amount
payment_amount = float(input("Enter the payment amount: "))

# Compute and display change
change = payment_amount - total_price
print(f'Change: ${change:.2f}')
