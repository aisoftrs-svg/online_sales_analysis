from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()

    # Promenjena imena i količine proizvoda
    p1 = Product("Gaming Laptop", 120000.0, 3)
    p2 = Product("Bežični Miš", 3500.0, 20)
    p3 = Product("Mehanička Tastatura", 8000.0, 8)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

