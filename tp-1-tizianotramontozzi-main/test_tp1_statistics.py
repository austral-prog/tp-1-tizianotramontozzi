import io
import unittest.mock
import exercise_statistics


class TestStatistics(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_statistics(self, mock_stdout):
        exercise_statistics.statistics()
        results = mock_stdout.getvalue().splitlines()
        self.assertAlmostEqual(float(results[0]), 14.5, places=2)  # promedio
        self.assertEqual(results[1], "23")  # máximo
        self.assertEqual(results[2], "8")  # mínimo
        self.assertEqual(results[3], "15")  # rango


if __name__ == '__main__':
    unittest.main()
