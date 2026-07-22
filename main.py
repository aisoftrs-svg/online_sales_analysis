import random
from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    manager = ProductManager()

    # Dodavanje proizvoda u inventar
    p1 = Product("Laptop", 90000.0, 5)
    p2 = Product("Miš", 2500.0, 15)
    p3 = Product("Tastatura", 5000.0, 10)
    p4 = Product("Monitor", 22000.0, 8)
    p5 = Product("Slušalice", 4500.0, 20)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    manager.add_product(p4)
    manager.add_product(p5)

    # Kreiranje instance klase Cart
    cart = Cart()

    # Nasumičan izbor 3 proizvoda iz dostupnih proizvoda u manager-u
    if len(manager.products) >= 3:
        random_products = random.sample(manager.products, 3)
        for p in random_products:
            cart.add_to_cart(p)

    # Ispis sadržaja korpe i ukupne vrednosti za naplatu
    cart.display_cart()
    print(f"\nUkupno za naplatu (korpa): {cart.calculate_total():.2f} RSD")