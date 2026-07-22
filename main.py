import random
from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    manager = ProductManager()

    # Zadržavamo izmenjene proizvode sa master grane
    p1 = Product("Gaming Laptop", 120000.0, 3)
    p2 = Product("Bežični Miš", 3500.0, 20)
    p3 = Product("Mehanička Tastatura", 8000.0, 8)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Zadržavamo funkcionalnost korpe sa add-cart-functionality grane
    cart = Cart()

    if len(manager.products) >= 3:
        random_products = random.sample(manager.products, 3)
        for p in random_products:
            cart.add_to_cart(p)

    cart.display_cart()
    print(f"\nUkupno za naplatu (korpa): {cart.calculate_total():.2f} RSD")