from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"Dodat proizvod: {product.name}")

    def remove_product(self, product_name: str):
        """Uklanja proizvod na osnovu imena."""
        initial_count = len(self.products)
        self.products = [p for p in self.products if p.name.lower() != product_name.lower()]

        if len(self.products) < initial_count:
            print(f"Proizvod '{product_name}' je uspešno uklonjen.")
        else:
            print(f"Proizvod '{product_name}' nije pronađen.")

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