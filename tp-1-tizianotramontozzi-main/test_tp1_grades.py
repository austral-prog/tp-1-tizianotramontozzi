import io
import unittest.mock
import exercise_grades


class TestGrades(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_grades(self, mock_stdout):
        exercise_grades.grades()
        results = mock_stdout.getvalue().splitlines()
        self.assertAlmostEqual(float(results[0]), 8.0, places=2)  # promedio
        self.assertEqual(results[1], "9")  # máximo
        self.assertEqual(results[2], "7")  # mínimo
        self.assertAlmostEqual(float(results[3]), 2.0, places=2)  # puntos faltantes


if __name__ == '__main__':
    unittest.main()
