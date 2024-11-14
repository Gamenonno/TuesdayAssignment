class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total_sum = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.total_sum += number

    def count_numbers(self) -> int:
        return self.numbers

    def get_sum(self) -> int:
        return self.total_sum

    def average(self) -> float:
        if self.numbers == 0:
            return 0
        return self.total_sum / self.numbers

def main():
    stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()

    print("Please type in integer numbers:")
    while True:
        number = int(input())
        if number == -1:
            break
        stats.add_number(number)
        if number % 2 == 0:
            even_stats.add_number(number)
        else:
            odd_stats.add_number(number)

    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", even_stats.get_sum())
    print("Sum of odd numbers:", odd_stats.get_sum())

# Example of running the main function
if __name__ == "__main__":
    main()
