def test_day_to_year():
    assert day_to_year(1) == 1970 # "January 1st 1970"
    assert day_to_year(366) == 1971 # "January 1st 1971"
    assert day_to_year(365 + 365 + 1) == 1972 # "January 1st 1972"
    assert day_to_year(365 + 365 + 366 + 1) == 1973 # "January 1st 1973"


'''
Let's go through what we're testing for.
Remember that these tests were given to you,
so they tell you a lot about how the program should behave.

1.  Test1: Adding just one day.
    This returns 1970, because we remain on"January1st1970".
    NOTE:Note that we did not go to Jan 2nd, which tells you
    alot about how we expect the program to work.

2. Test2: Adding 366 days, i.e.A leap year.
    1970 was NOT a leapyear, as such we end on Jan 1 1971.
    If it was aleap year, where would we actually end?

3. Test3: Adding 731 days. This can be split into 365 + 365 + 1 days.
    The first 365 days take us to 31/12/1970.
    65 days after this we will be on 31/12/1971
    (1971 is not a leap year either).
    1 day after this we will be on 01/01/1972.

4. Test4: Adding 1097 days. This can be split into
    365 + 365 + 366 + 1 days. Since 1972 is a leap year,
    we should end on January 1st 1973 - this is because of the + 1.

So, what have we NOT tested for?
This is where the "Zune bug" comes in.
The codes purpose is to repeatedly decrement the days count by 365
in common years and by 366 in leap years.
Increment the year by 1 each time.
However, what happens when the initial
value of days is 366 AND we begin on a leap year?

As an example, we will assume we are on 1972
and try to add 366 days to this.
Since 366 is greater than 365,
we pass the (while days > 365) check.
The IsLeapYear function also returns true.
Now we try the test (days > 366), and
this returns false we do not decrement
days nor increment year. We simply return
to the head of the while loop, where we find that
days is unchanged and greater than 365,
and so we enter an infinite loop.

This is called the zune bug biggest its a
bug that caused microsofts music playing
systems to run into an infinity
loop back in 1980. Lolz What next?
We need to make a test which takes
us to a leap year from 1970 and then adds 366 days...
'''

def test_new():
    #Theassertthatcatchesthezunebug
    assert day_to_year(365 + 365 + 366) == 1972 # Shouldreturn "December 31st 1972"