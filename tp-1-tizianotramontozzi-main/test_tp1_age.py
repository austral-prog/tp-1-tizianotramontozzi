import io
import unittest.mock
import exercise_age


class TestAge(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_age(self, mock_stdout):
        exercise_age.age()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "300")  # meses
        self.assertEqual(results[1], "9125")  # días
        self.assertEqual(results[2], "219000")  # horas
        self.assertEqual(results[3], "13140000")  # minutos


if __name__ == '__main__':
    unittest.main()
