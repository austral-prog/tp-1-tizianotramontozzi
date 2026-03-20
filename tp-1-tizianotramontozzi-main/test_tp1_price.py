import io
import unittest.mock
import exercise_price


class TestPrice(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_price(self, mock_stdout):
        exercise_price.price()
        results = mock_stdout.getvalue().splitlines()
        self.assertAlmostEqual(float(results[0]), 21.0, places=2)  # impuesto
        self.assertAlmostEqual(float(results[1]), 121.0, places=2)  # subtotal
        self.assertAlmostEqual(float(results[2]), 12.1, places=2)  # propina
        self.assertAlmostEqual(float(results[3]), 133.1, places=2)  # precio final


if __name__ == '__main__':
    unittest.main()
