from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()

    # Dodavanje proizvoljnih proizvoda
    p1 = Product("Laptop", 90000.0, 5)
    p2 = Product("Miš", 2500.0, 15)
    p3 = Product("Tastatura", 5000.0, 10)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Prikaz proizvoda i ukupne vrednosti
    manager.display_all_products()
    print(f"\nUkupna vrednost inventara: {manager.get_total_value():.2f} RSD")