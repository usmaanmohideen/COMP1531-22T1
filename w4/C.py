from calendar import isleap

ORIGIN_YEAR = 1970

def day_to_year(days):
    year = ORIGIN_YEAR

    while days > 365:
        if isleap(year):
            if days > 366:
                days -= 366
                year += 1
        else:
            days -= 365
            year += 1

    return year

from day_to_year import day_to_year

def test_day_to_year():
    assert day_to_year(1) == 1970 # "January 1st 1970"
    assert day_to_year(366) == 1971 # "January 1st 1971"
    assert day_to_year(365 + 365 + 1) == 1972 # "January 1st 1972"
    assert day_to_year(365 + 365 + 366 + 1) == 1973 # "January 1st 1973"

'''
1.  Test1: Adding just one day.
        assert day_to_year(1) == 1970 # "January 1st 1970"

    This returns 1970, because we remain on " January 1st 1970".
    NOTE:Note that we did not go to Jan 2nd, which tells you
    alot about how we expect the program to work.

2. Test2: Adding 366 days, i.e.A leap year.
        assert day_to_year(366) == 1971 # "January 1st 1971"

    1970 was NOT a leapyear, as such we end on Jan 1 1971.
    If it was aleap year, where would we actually end?

3. Test3:
        assert day_to_year(365 + 365 + 1) == 1972 # "January 1st 1972"

    Adding 731 days. This can be split into 365 + 365 + 1 days.
    The first 365 days take us to 31/12/1970.
    365 days after this we will be on 31/12/1971
    (1971 is not a leap year either).
    1 day after this we will be on 01/01/1972.

4. Test4:
        assert day_to_year(365 + 365 + 366) == 31st Dec [1972]

    Adding 1097 days. This can be split into
    365 + 365 + 366 + 1 days. Since 1972 is a leap year,
    we should end on January 1st 1973 - this is because of the + 1.
'''