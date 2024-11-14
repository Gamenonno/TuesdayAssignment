class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.initial_value = initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial_value

# Example of the class in action
counter = DecreasingCounter(10)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()

# Further examples to demonstrate additional functionalities
print("\nTesting no negative values:")
counter = DecreasingCounter(2)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()

print("\nSetting the value to zero:")
counter = DecreasingCounter(100)
counter.print_value()
counter.set_to_zero()
counter.print_value()

print("\nResetting the counter to its original value:")
counter = DecreasingCounter(55)
counter.decrease()
counter.decrease()
counter.decrease()
counter.decrease()
counter.print_value()
counter.reset_original_value()
counter.print_value()
