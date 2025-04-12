'''Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing
methods to add a new date, delete a given date, modify a date, and perform a query on a given date is
required.  A query on a given date allows for retrieving a given new date. Note that a date is an object for your
database; it must be instantiated from a string.
'''

class date:
    def __init__(self):
        self.day: int = 1
        self.month: str = 1
        self.year: str = 1900
    
    def change_date(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self) -> str:
        day_str = f"0{self.day}" if self.day < 10 else f"{self.day}"
        month_str = f"0{self.month}" if self.day < 10 else f"{self.month}"
        return f"{day_str}.{month_str}.{self.year}"

if __name__ == "__main__":
    year1: date = date()
    year1.change_date(1, 1, 2025)
    print(year1)