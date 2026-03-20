import io
import unittest.mock
import exercise_length


class TestLength(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_length(self, mock_stdout):
        exercise_length.length()
        results = mock_stdout.getvalue().splitlines()
        self.assertAlmostEqual(float(results[0]), 1.0, places=2)  # kilómetros
        self.assertAlmostEqual(float(results[1]), 0.62, places=2)  # millas
        self.assertAlmostEqual(float(results[2]), 3280.84, places=2)  # pies
        self.assertAlmostEqual(float(results[3]), 39370.08, places=2)  # pulgadas


if __name__ == '__main__':
    unittest.main()
