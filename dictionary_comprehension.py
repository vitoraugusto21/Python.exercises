# copy, sorted, produtos.sort
# Exercise
# Increase the prices of the following products by 10% 
# Generate new_products by deep copy 
products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

# Sort the products by descending name (from highest to lowest) 
# Generate products_sorted_by_name by deep copy 

# Sort the products by ascending price (from lowest to highest)
# Generate products_ordered_by_price by deep copy

import copy

new_products = [ #Increase 10%
    {**p, 'price': round(p['price'] * 1.1,2)}
    for p in copy.deepcopy(products)
]

products_sorted_by_name = sorted( # Order by name (from highest to lowest)
    copy.deepcopy(products),
    key=lambda p: p['name'],
    reverse=True
)

products_sorted_by_price = sorted( # Order by price
    copy.deepcopy(products),
    key=lambda p: p['price']
)

print(*products, sep='\n')
print()
print(*new_products, sep='\n')
print()
print(*products_sorted_by_name, sep='\n')
print()
print(*products_sorted_by_price, sep='\n')
print()