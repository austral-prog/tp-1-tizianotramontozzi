import io
import unittest.mock
import exercise_swap


class TestSwap(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_swap(self, mock_stdout):
        exercise_swap.swap()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "10")  # x original
        self.assertEqual(results[1], "20")  # y original
        self.assertEqual(results[2], "20")  # x intercambiado
        self.assertEqual(results[3], "10")  # y intercambiado


if __name__ == '__main__':
    unittest.main()
