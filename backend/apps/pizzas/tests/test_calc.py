from unittest import TestCase
from unittest.mock import MagicMock, patch

from ..service import calc, math


class CalcTestCase(TestCase):
    # @patch('apps.pizzas.service.cos')
    @patch.object(math, 'cos')
    def test_plus(self, mock_cos: MagicMock):
        mock_cos.return_value = 66
        res = calc(5, 6, '+')
        self.assertEqual(res, 66)

    def test_minus(self):
        res = calc(5, 6, '-')
        self.assertEqual(res, -1)

    def test_multiply(self):
        res = calc(5, 6, '*')
        self.assertEqual(res, 30)