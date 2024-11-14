class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional

# Example of creating instances of the classes
checklist_example = Checklist(header="Shopping List", entries=["Milk", "Eggs", "Bread"])
customer_example = Customer(id="C001", balance=150.50, discount=10)
cable_example = Cable(model="CAT6", length=1.5, max_speed=1000, bidirectional=True)

print(f"Checklist - Header: {checklist_example.header}, Entries: {checklist_example.entries}")
print(f"Customer - ID: {customer_example.id}, Balance: {customer_example.balance}, Discount: {customer_example.discount}")
print(f"Cable - Model: {cable_example.model}, Length: {cable_example.length}, Max Speed: {cable_example.max_speed}, Bidirectional: {cable_example.bidirectional}")
