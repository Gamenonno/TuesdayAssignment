def list_years(dates: list) -> list:
    # Extract the years from the date objects
    years = [date.year for date in dates]
    # Sort the years in chronological order
    years.sort()
    return years

# Example of the function in action
from datetime import datetime

dates = [
    datetime(2022, 5, 17),
    datetime(2018, 11, 2),
    datetime(2023, 8, 24),
    datetime(2019, 1, 15)
]

print(list_years(dates))
