import unittest
from api.viewsets import limit_credit, get_limit
# Create your tests here.

class TestCreditCard(unittest.TestCase):
    def setUp(self):
        self.score_1 = 1
        self.score_2 = 299
        self.score_3 = 300
        self.score_4 = 599
        self.score_5 = 600
        self.score_6 = 850
        self.score_7 = 851
        self.score_8 = 950
        self.score_9 = 951
        self.score_10 = 999
        self.income = 8500


    def test_all_limits_integer(self):
        for limit in limit_credit:
            self.assertTrue(type(limit) is int)
            self.assertGreaterEqual(limit, 1)


    def test_limit_1(self):
        self.assertEqual('Reprovado', limit_credit[get_limit(self.score_1)](self.income))
        self.assertEqual('Reprovado', limit_credit[get_limit(self.score_2)](self.income))

    def test_limit_2(self):
        self.assertEqual('R$ 1000', limit_credit[get_limit(self.score_3)](self.income))
        self.assertEqual('R$ 1000', limit_credit[get_limit(self.score_4)](self.income))

    def test_limit_3(self):
        self.assertEqual('R$ 4250', limit_credit[get_limit(self.score_5)](self.income))
        self.assertEqual('R$ 4250', limit_credit[get_limit(self.score_6)](self.income))

    def test_limit_4(self):
        self.assertEqual('R$ 17000', limit_credit[get_limit(self.score_7)](self.income))
        self.assertEqual('R$ 17000', limit_credit[get_limit(self.score_8)](self.income))

    def test_limit_5(self):
        self.assertEqual('R$ 1000000', limit_credit[get_limit(self.score_9)](self.income))
        self.assertEqual('R$ 1000000', limit_credit[get_limit(self.score_10)](self.income))
