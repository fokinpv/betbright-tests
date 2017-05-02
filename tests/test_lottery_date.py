import unittest
from datetime import datetime

from betbright_tests.lottery_date import next_lottery_date

DATE_FORMAT = '%Y-%m-%d'
strptime = datetime.strptime


class TestLotteryDay(unittest.TestCase):

    def test_next_lottery_day_default(self):
        next_date = next_lottery_date()

        isoweekday = next_date.isoweekday()

        self.assertTrue(isoweekday == 3 or isoweekday == 5)

    def test_next_lottery_day(self):
        date_str = '2017-05-02'
        next_date_str = '2017-05-03'
        date = strptime(date_str, DATE_FORMAT)

        next_date = next_lottery_date(date)

        self.assertEqual(next_date, strptime(next_date_str, DATE_FORMAT))

    def test_next_lottery_day_wednesday(self):
        """If given date is Wednesday"""
        date_str = '2017-05-03'
        next_date_str = '2017-05-05'
        date = strptime(date_str, DATE_FORMAT)

        next_date = next_lottery_date(date)

        self.assertEqual(next_date, strptime(next_date_str, DATE_FORMAT))
