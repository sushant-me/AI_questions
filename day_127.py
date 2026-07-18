class ShoppingCart:
    """Create a ShoppingCart class."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    def get_items(self):
        return self.items