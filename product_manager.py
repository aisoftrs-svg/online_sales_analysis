from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"Dodat proizvod: {product.name}")

    def display_all_products(self):
        if not self.products:
            print("Nema dostupnih proizvoda u inventaru.")
            return
        print("\n--- Lista svih proizvoda ---")
        for product in self.products:
            product.display_info()

    def get_total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        return total