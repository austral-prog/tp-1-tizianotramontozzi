import io
import unittest.mock
import exercise_circle


class TestCircle(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_circle(self, mock_stdout):
        exercise_circle.circle()
        results = mock_stdout.getvalue().splitlines()
        self.assertAlmostEqual(float(results[0]), 78.54, places=2)  # área
        self.assertAlmostEqual(float(results[1]), 31.42, places=2)  # circunferencia


if __name__ == '__main__':
    unittest.main()
