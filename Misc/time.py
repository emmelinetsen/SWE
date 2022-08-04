from datetime import date, datetime
import calendar

# date_string = "2012-12-12"
# d = datetime.fromisoformat(date_string)
# d2 = datetime.fromisoformat("2012-12-13")
# # print (datetime.fromisoformat(date_string))
# # print (d.month)
# # print ((d - d2).days)
# #
# # print(float (4/3))
#
#
# month = "2012-12"
# month_split = month.split('-')
# # print(month_split)
# # print(calendar.monthrange(int(month_split[0]), int(month_split[1]))[1])
# month_in_datetime = month + "-01"
# # print(datetime.fromisoformat(month_in_datetime))
#
# user_signed_up = [
#     {
#         'id': 1,
#         'name': 'Employee #1',
#         'activated_on': datetime.fromisoformat(date_string),
#         'deactivated_on': None,
#         'customer_id': 1,
#     },
#     {
#         'id': 2,
#         'name': 'Employee #2',
#         'activated_on': datetime.fromisoformat(date_string),
#         'customer_id': 1,
#     }]
#
# # print(user_signed_up[0]['activated_on'])
#
print((date(2018, 11, 4) - date(2019, 1, 5)).days)
# print(round(12.3434343432,2))

month = "2022-01"
month_split = month.split('-') # split to year, day
#   month_in_datetime = datetime.fromisoformat(month + "-01")
days_in_month = calendar.monthrange(int(month_split[0]), int(month_split[1]))[1]
# print(days_in_month)
# for i in range(days_in_month):
#     print(i)


import datetime
import calendar

# returns the total monthly bill for a customer
def bill_for(month, active_subscription, users):
    if len(users) == 0:
        return float(0.00)

    month_split = month.split('-') # split to year, day
    #   month_in_datetime = datetime.fromisoformat(month + "-01")
    days_in_month = calendar.monthrange(int(month_split[0]), int(month_split[1]))[1]

    bill = 0
    # calculate daily rate
    rate = daily_rate(month_split, active_subscription)

    # iterate through the entire month

    for day in range(1,days_in_month+1):
        day_in_datetime = datetime.date(int(month_split[0]), int(month_split[1]), day)
        # calculate the # of active users
        num_users_today = 0
        for user in users:
            # if user has is deactivated today, count user
            if user['deactivated_on'] and (user['deactivated_on'] - day_in_datetime).days == 0:
                num_users_today += 1
            # if the date is on or after the current day and not deactivated
            if ((user['activated_on'] - day_in_datetime).days) <= 0 and user['deactivated_on'] is None:
                num_users_today += 1

        # multiply by the daily rate and add to sum
        bill += rate * num_users_today
    return round(bill, 2)




    pass

def daily_rate(month_split, active_subscription):

    return float(active_subscription['monthly_price_in_dollars']/calendar.monthrange(int(month_split[0]), int(month_split[1]))[1])


####################
# Helper functions #
####################

def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(datetime.date(2019, 2, 7))  # Feb 7
    datetime.date(2019, 2, 1)                          # Feb 1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)

def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    >>> last_day_of_month(datetime.date(2019, 2, 7))  # Feb  7
    datetime.date(2019, 2, 28)                        # Feb 28

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)

def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    >>> next_day(datetime.date(2019, 2, 7))   # Feb 7
    datetime.date(2019, 2, 8)                 # Feb 8

    >>> next_day(datetime.date(2019, 2, 28))  # Feb 28
    datetime.date(2019, 3, 1)                 # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)


import unittest
import datetime
# from solution import bill_for

user_signed_up = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

constant_users = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

new_plan = {
    'id': 1,
    'customer_id': 1,
    'monthly_price_in_dollars': 4
}

no_users = []

# Note: the class must be called Test
class Test(unittest.TestCase):
    def test_works_when_the_customer_has_no_active_users_during_the_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, no_users), 0.00, delta=0.01)

    def test_works_when_everything_stays_the_same_for_a_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, constant_users), 8.00, delta=0.01)

    def test_works_when_a_user_is_activated_during_the_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, user_signed_up), 10.84, delta=0.01)
