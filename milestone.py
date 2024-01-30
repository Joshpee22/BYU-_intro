# Ask the user for the price of a child and an adult meal  child_meal_price = float(input("Enter the price of a child's meal: $"))                                               adult_meal_price = float(input("Enter the price of an adult's meal: $"))                                                                                                         # Ask the user for the number of children and adults       num_children = int(input("Enter the number of children: "))num_adults = int(input("Enter the number of adults: "))

# Calculate subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# Ask the user for the sales tax rate
sales_tax_rate = float(input("Enter the sales tax rate in percentage: "))

# Calculate sales tax
sales_tax = (subtotal * sales_tax_rate) / 100

# Calculate total price
total_price = subtotal + sales_tax

# Display subtotal, sales tax, and total
print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total_price:.2f}')

# Ask the user for the payment amount
payment_amount = float(input("\nEnter the payment amount: $"))

# Compute and display change
change = payment_amount - total_price
print(f'Change: ${change:.2f}')

# Additional features: Display a thank you message and provide a receipt
print("\nThank you for dining with us!")
print("\nReceipt:")
print(f'Child Meal Cost: ${child_meal_price:.2f} x {num_children} = ${child_meal_price * num_children:.2f}')
print(f'Adult Meal Cost: ${adult_meal_price:.2f} x {num_adults} = ${adult_meal_price * num_adults:.2f}')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax ({sales_tax_rate}%): ${sales_tax:.2f}')
print(f'Total: ${total_price:.2f}')
print(f'Payment: ${payment_amount:.2f}')
print(f'Change: ${change:.2f}')
