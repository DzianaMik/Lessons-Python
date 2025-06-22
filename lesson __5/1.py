product1 = input("Ввести 1 товар и цена: ")
product2 = input("Ввести 2 товар и цена: ")
product3 = input("Ввести 3 товар и цена: ")
products = {}
for part in [product1, product2, product3]:
    name, price = part.split()
    products[name] = float(price)
print("\nСписок товаров:")
for name, price in products.items():
    print(f"{name} - {price}")
price = input("\nВведите название товара увеличенного на 15%: ")
if price in products:
   increased = products[price] * 1.15
   print(f"Цена{price} увеличенна на 15%: {increased}")
total = sum(products.values())
print(f"\nСумма всех товаров: {total}")