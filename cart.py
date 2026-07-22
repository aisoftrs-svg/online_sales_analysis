from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product: Product):
        self.cart_items.append(product)
        print(f"Proizvod '{product.name}' je dodat u korpu.")

    def calculate_total(self):
        # Ukupna vrednost korpe (zbir cena svih proizvoda u korpi)
        return sum(product.price for product in self.cart_items)

    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        print("\n--- Sadržaj korpe ---")
        for item in self.cart_items:
            item.display_info()