import io
import unittest.mock
import exercise_currency


class TestCurrency(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_currency(self, mock_stdout):
        exercise_currency.currency()
        results = mock_stdout.getvalue().splitlines()
        self.assertAlmostEqual(float(results[0]), 6.67, places=2)  # dólares
        self.assertAlmostEqual(float(results[1]), 6.25, places=2)  # euros
        self.assertAlmostEqual(float(results[2]), 40.0, places=2)  # reales


if __name__ == '__main__':
    unittest.main()
