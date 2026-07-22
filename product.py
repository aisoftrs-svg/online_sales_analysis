class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Proizvod: {self.name} | Cena: {self.price:.2f} RSD | Količina: {self.quantity}")

    def update_quantity(self, amount: int):
        self.quantity += amount
        print(f"Ažurirana količina za {self.name}: nova količina je {self.quantity}.")