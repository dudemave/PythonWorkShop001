

import unittest

from read_csv_data import PostalData
from datetime import datetime

class TestStringMethods(unittest.TestCase):

    def test_split_is_Ex(self):

        test_row = [1, 'name', 'other_name',
                    123456789, '2020-12-24']

        test_time_1 = datetime.fromisoformat('2002-06-20')
        test_time_2 = datetime.fromisoformat('2022-06-20')

        pp = PostalData(test_row)

        self.assertFalse(pp.user_is_expired(test_time_1))
        self.assertTrue(pp.user_is_expired(test_time_2))



if __name__ == '__main__':
    unittest.main()
