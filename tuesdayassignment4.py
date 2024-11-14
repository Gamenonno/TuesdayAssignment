class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, quantity: int):
        self.items.append((item_name, quantity))

def total_units(my_list: ShoppingList) -> int:
    total = 0
    for item in my_list.items:
        total += item[1]  
    return total


my_shopping_list = ShoppingList()
my_shopping_list.add_item("Apples", 4)
my_shopping_list.add_item("Bananas", 2)
my_shopping_list.add_item("Oranges", 6)

print(total_units(my_shopping_list))  
