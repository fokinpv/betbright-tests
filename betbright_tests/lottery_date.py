"""Date Calculation.
The Irish lottery draw takes place twice weekly on a Wednesday and a
Saturday at 8pm. Write a function that calculates and returns the next
valid draw date based on an optional supplied date time parameter. If no
supplied date is provided, assume current date time.
"""
import datetime


def next_lottery_date(date=None):
    """Calculates and returns the next
    valid draw date based on an optional supplied date time parameter.
    """
    WEDNESDAY = 3
    FRIDAY = 5

    if not date:
        date = datetime.datetime.today()

    # If given date is Wednesday or Friday
    # We want to get next draw date
    date += datetime.timedelta(1)
    while (date.isoweekday() != WEDNESDAY) and (date.isoweekday() != FRIDAY):
        date += datetime.timedelta(1)

    return date
