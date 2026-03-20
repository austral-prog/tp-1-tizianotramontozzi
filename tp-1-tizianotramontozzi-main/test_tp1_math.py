import io
import unittest.mock
import exercise_math


class TestMath(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_math(self, mock_stdout):
        exercise_math.math()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "64")  # suma
        self.assertEqual(results[1], "50")  # diferencia
        self.assertEqual(results[2], "399")  # producto
        self.assertAlmostEqual(float(results[3]), 32.0, places=2)  # promedio
        self.assertEqual(results[4], "8")  # cociente entero
        self.assertEqual(results[5], "1")  # resto
        self.assertAlmostEqual(float(results[6]), 8.14, places=2)  # división real


if __name__ == '__main__':
    unittest.main()
