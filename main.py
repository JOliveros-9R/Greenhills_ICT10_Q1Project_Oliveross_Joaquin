from pyscript import display, document

# Restaurant details
restaurant_name = "Drive-IN/OUT" #STRING
owner_name = "Joaquin Oliveros" #STRING
year_established = 2000 #STRING

# Menu and details
menu_items = ["Double Cheese Burger", "Chicken Wings", "Iced Lemon Tea", "Iced Tea"] #LIST
menu_prices = [200, 250, 90, 80] #LIST
has_delivery = True #STRING
business_hours = ["9:00 AM", "9:30 PM"] #STRING
allergens = ["dairy", "egg", "meat"] #STRING
tax_rate = 0.12 #STRING

display(f"{restaurant_name}", target='restaurant-title')
display(f"owned by {owner_name}", target='owner-info')
display(f"Year established:  {year_established}", target='year-info')
display(f"Menu item: {menu_items[1]} costs ₱{menu_prices[1]}", target='menu-table')
display(f"Menu item: {menu_items[2]} costs ₱{menu_prices[2]}", target='menu-table')
display(f"Menu item: {menu_items[3]} costs ₱{menu_prices[3]}", target='menu-table')
display(f"Delivery available: {has_delivery}", target='menu-table')
display(f"Business hours: {business_hours[0]} - {business_hours[1]}", target='hours-info')
display(f"Allergens: {', '.join(allergens)}", target='hours-info')
display(f"Tax rate: {int(tax_rate * 100)}%", target='hours-info')

