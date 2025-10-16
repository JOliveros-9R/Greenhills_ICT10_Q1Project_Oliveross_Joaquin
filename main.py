from pyscript import display, document

# Basic info for homepage
restaurant = "Drive-IN/OUT"
owner = "Joaquin Oliveros"
year = 2000

menu = ["Double Cheese Burger", "Chicken Wings", "Iced Lemon Tea", "Iced Tea"]
prices = [200, 250, 90, 80]

# Show homepage info if elements exist
if document.querySelector("#restaurant-title"):
    display(restaurant, target="restaurant-title")
    display(f"owned by {owner}", target="owner-info")
    display(f"Year established: {year}", target="year-info")

    for i in range(len(menu)):
        display(f"{menu[i]} / ₱{prices[i]}", target="menu-table")

    display("Delivery available: True", target="menu-table")
    display("Business hours: 9:00 AM - 9:30 PM", target="hours-info")
    display("Allergens: dairy, egg, meat", target="hours-info")
    display("Tax rate: 12%", target="hours-info")
