def calculate_total():
    # Get user input for subtotal
    subtotal = float(input("Enter Subtotal: $"))

    # Get user input for tax rate
    tax_rate = float(input("Enter Tax Rate (%): "))

    # Calculate tax and total
    tax = (subtotal * tax_rate) / 100
    total = subtotal + tax

    # Display results
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

# Call the function to calculate total
calculate_total()
