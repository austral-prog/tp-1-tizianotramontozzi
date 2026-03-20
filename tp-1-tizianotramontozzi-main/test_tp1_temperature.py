import io
import unittest.mock
import exercise_temperature


class TestTemperature(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_temperature(self, mock_stdout):
        exercise_temperature.temperature()
        results = mock_stdout.getvalue().splitlines()
        self.assertAlmostEqual(float(results[0]), 77.0, places=2)  # fahrenheit
        self.assertEqual(results[1], "25")  # celsius original


if __name__ == '__main__':
    unittest.main()
