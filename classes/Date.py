from modules.date_utils import *
from classes.CustomExceptions import *


# ## Date Class
class Date:
    def __init__(self, day, month, year):
        if type(day) != type(1) or type(month) != type(1) or type(year) != type(1):
            print("Date must be initialized with numbers")
            return
        if (month < 1) or (month > 12):
            raise DateException("Month must be between 1 and 12")
            # print("Month must be between 1 and 12")
            # return
        if is_leap_year(year):
            if (day < 0) or (day > days_in_month_leap_year[month - 1]):
                print("day must be between 1 and ", days_in_month_leap_year[month - 1])
                return
        else:
            if (day < 0) or (day > days_in_month[month - 1]):
                print("day must be between 1 and ", days_in_month[month - 1])
                return
        self.day = day
        self.month = month
        self.year = year

    def __gt__(self, other):
        """ Overloading operator > for dates """
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
        return False

    def __lt__(self, other):
        """ Overloading operator < for dates """
        return other > self

    def __eq__(self, other):
        """Overloading operator == for dates"""
        return (self.year == other.year) and (self.month == other.month) and (self.day == other.day)

    def __ne__(self, other):
        """Overloading operator != for dates"""
        return not (self == other)

    def __le__(self, other):
        """ Overloading operator <= for dates """
        return (self < other) or (self == other)

    def __ge__(self, other):
        """ Overloading operator >= for dates """
        return (self > other) or (self == other)

    def __str__(self):
        return str(self.day) + "." + str(self.month) + "." + str(self.year)
