from unittest import TestCase
from unittest.mock import MagicMock, patch

from ..service import calc, math


class CalcTestCase(TestCase):
    @patch.object(math, 'cos')
    def test_plus(self, calc_mock: MagicMock):
        calc_mock.return_value = 55
        res = calc(2, 1, '+')
        self.assertEqual(res, 55)

    def test_multiply(self):
        res = calc(2, 1, '*')
        self.assertEqual(res, 2)

    def test_minus(self):
        res = calc(2, 1, '-')
        self.assertEqual(res, 1)
