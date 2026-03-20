import io
import unittest.mock
import exercise_time


class TestTime(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_time(self, mock_stdout):
        exercise_time.time()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "1")  # horas
        self.assertEqual(results[1], "1")  # minutos
        self.assertEqual(results[2], "5")  # segundos


if __name__ == '__main__':
    unittest.main()
