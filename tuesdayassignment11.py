class Person:
    def __init__(self, name: str):
        self.name = name

    def return_first_name(self) -> str:
        return self.name.split()[0]

    def return_last_name(self) -> str:
        return self.name.split()[1]

# Example of the class in action
person = Person("John Doe")
print(f"First name: {person.return_first_name()}")
print(f"Last name: {person.return_last_name()}")
