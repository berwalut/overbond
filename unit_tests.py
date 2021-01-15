import io
import unittest
import unittest.mock

from challenge1 import corporate_bond_spread, find_the_closest_value_index
from challenge2 import spread_to_government_bond_curve, find_the_closest_value_index_low


class TestChallenge(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        corporate_bond_spread([['C1', 'corporate', '10.3', '5.3']], [['G1', 'government', '9.4', '3.7'], ['G2', 'government', '12', '4.8']])
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_corporate_bond_spread(self):
        self.assert_stdout(1, 'bond,benchmark,spread_to_benchmark\nC1,G1,1.60%\n')

    def test_find_the_closest_value_index(self):
        expected = find_the_closest_value_index(10.3, [['G1', 'government', '9.4', '3.7'], ['G2', 'government', '12', '4.8']])
        self.assertEqual(0, expected)


class TestChallenge2(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        spread_to_government_bond_curve([['C1', 'corporate', '10.3', '5.3'], ['C2', 'corporate', '15.2', '8.3']], [['G1', 'government', '9.4', '3.7'], ['G2', 'government', '12', '4.8'], ['G3', 'government', '16.3', '5.5']])
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_spread_to_government_bond_curve(self):
        self.assert_stdout(1, 'bond,spread_to_curve\nC1,1.22%\nC2,2.98%\n')

    def test_find_the_closest_value_index(self):
        expected = find_the_closest_value_index_low(15.2, [['G1', 'government', '9.4', '3.7'], ['G2', 'government', '12', '4.8'], ['G3', 'government', '16.3', '5.5']])
        self.assertEqual(1, expected)        
        