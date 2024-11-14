class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount

def main():
    # Creating lunch cards for Peter and Grace
    peters_card = LunchCard(20)
    graces_card = LunchCard(30)

    # Peter eats a special lunch
    peters_card.eat_special()
    # Grace eats a regular lunch
    graces_card.eat_lunch()

    # Printing the balance on each card
    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")

    # Peter deposits 20 euros
    peters_card.deposit_money(20)
    # Grace eats the special
    graces_card.eat_special()

    # Printing the balance on each card
    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")

    # Peter eats two regular lunches
    peters_card.eat_lunch()
    peters_card.eat_lunch()
    # Grace deposits 50 euros
    graces_card.deposit_money(50)

    # Printing the balance on each card
    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")

# Running the main function
if __name__ == "__main__":
    main()
