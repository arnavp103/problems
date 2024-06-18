"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
     but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def dayofweek(day: int, month: int, year: int) -> int:
    """Returns the day of the week for a given date"""
    # 0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday
    # Zeller's Congruence
    if month < 3:
        month += 12
        year -= 1

    K = year % 100
    J = year // 100

    h = (day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7

    return h


def solution():
    """uses the formula for calculating the day of the week for a given date"""
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            # this whole section is unnecessary
            days_in_month = []
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            for day in range(1, days_in_month[month - 1] + 1):
                # i could've just skipped the days in month thing
                # and just only considered the first day of the month huh
                # but i found zeller's congruence after the fact
                if dayofweek(day, month, year) == 0 and day == 1:
                    count += 1

    return count


print(solution())

# 171 - correct
