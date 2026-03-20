import io
import unittest.mock
import exercise_triangle


class TestTriangle(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_triangle(self, mock_stdout):
        exercise_triangle.triangle()
        results = mock_stdout.getvalue().splitlines()
        self.assertAlmostEqual(float(results[0]), 30.0, places=2)  # área


if __name__ == '__main__':
    unittest.main()
