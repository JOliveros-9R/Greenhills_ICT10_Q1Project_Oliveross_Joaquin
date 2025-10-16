from pyscript import display, document 

products_prices = {"Double Cheese Burger": 200.0, "Chicken Wings": 250.0, "Lemon Iced Tea": 90.0, "Iced Tea": 80.0} 
tax_rate = 12.0  

# Order Form: Order Selection and Calculations
def order(e):
    document.getElementById('summary').innerHTML = "" 

    total = 0.0 

    # Checkbox Selection With Tax Calculations
    if document.getElementById("Double Cheese Burger").checked:
        total += products_prices["Double Cheese Burger"] * (tax_rate / 100)
    if document.getElementById("Chicken Wings").checked:
        total += products_prices["Chicken Wings"] * (tax_rate / 100)
    if document.getElementById("Lemon Iced Tea").checked:
        total += products_prices["Lemon Iced Tea"] * (tax_rate / 100)
    if document.getElementById("Iced Tea").checked:
        total += products_prices["Iced Tea"] * (tax_rate / 100)

    # Customer Details
    customer_name = document.getElementById("customerName").value.strip() 
    customer_address = document.getElementById("customerAddress").value.strip()
    customer_number = document.getElementById("customerNumber").value.strip() 

    if not customer_name or not customer_address or not customer_number:
        display("Please enter all required fields before checkout.", target="summary")
        return

    # Display Order Summary and Total Order
    display(f"Order for: {customer_name}", target="summary")
    display(f"Address: {customer_address}", target="summary")
    display(f"Contact Number: {customer_number}", target="summary")
    display(f"Total: ₱{total:.1f}", target="summary")