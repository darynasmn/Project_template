import unittest
import pandas as pd
from app.io.input import read_from_file_with_builtin, read_from_file_with_pandas

class TestInputFunctions(unittest.TestCase):

    def test_read_from_file_with_builtin_success(self):

        file_path = "data/test.txt"
        expected_content = "Test content"
        with open(file_path, 'w') as file:
            file.write(expected_content)

        actual_content = read_from_file_with_builtin(file_path)

        self.assertEqual(actual_content, expected_content)

    def test_read_from_file_with_builtin_file_not_found(self):

        non_existing_file_path = "data/non_existing_file.txt"

        with self.assertRaises(FileNotFoundError):
            read_from_file_with_builtin(non_existing_file_path)


    def test_read_from_file_with_builtin_exception(self):

        invalid_file_path = "invalid_file_path.txt"

        with self.assertRaises(Exception):
            read_from_file_with_builtin(invalid_file_path)

    def test_read_from_file_with_pandas_success(self):

        file_path = "data/test_csv.csv"

        expected_data = pd.DataFrame({'Name': ["Vlad", "Daryna", "Maria", "Mark", "Katya"], 'Grade': [10, 12, 5, 8, 9]})
        expected_data.to_csv(file_path, index=False)

        actual_data = read_from_file_with_pandas(file_path)

        self.assertTrue(expected_data.equals(actual_data))

    def test_read_from_file_with_pandas_invalid_data(self):

        file_path = "data/test_csv.csv"

        expected_data = pd.DataFrame({'Name': ["Vlad", "Daryna", "Maria", "Mark", "Katya"], 'Grade': [11, 12, 5, 8, 9]})

        with self.assertRaises(AssertionError):
            actual_data = read_from_file_with_pandas(file_path)
            self.assertTrue(expected_data.equals(actual_data))

    def test_read_from_file_with_pandas_exception(self):

        invalid_file_path = "invalid_file_path.csv"

        with self.assertRaises(Exception):
            read_from_file_with_pandas(invalid_file_path)

if __name__ == '__main__':
    unittest.main()
