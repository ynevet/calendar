# ## Module Functions
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_month_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]

name_to_days_num = {}
for i in range(12):
    name_to_days_num[month_names[i]] = days_in_month[i]


def get_num_of_days_in_momnth(month_name):
    """ Returns the number of days
    in a given month """
    if month_name in name_to_days_num:
        return name_to_days_num[month_name]
    else:
        print("No such Month")


def get_following_month(month_name):
    """ Returns the name of the following month
    of a given month """
    if month_name in name_to_days_num:
        month_index = month_names.index(month_name)
        return month_names[(month_index + 1) % 12]
    else:
        print("No such Month")


def is_leap_year(year):
    """ Returns True if the year is a leap year
    False otherwise """
    return (year % 4 == 0) and (year % 1000 != 0)
