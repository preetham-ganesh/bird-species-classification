# authors_name = 'Preetham Ganesh'
# project_title = 'Comparison of Approaches towards Classification of Birds Species'
# email = 'preetham.ganesh2021@gmail.com'


import os

import unittest

from utils import check_directory_path_existence


class TestDevFunctions(unittest.TestCase):
    """Tests functions in dev directory."""

    def test_check_directory_path_existence(self) -> None:
        """Tests check_directory_path_existence function from utils.py with multiple test cases.

        Args:
            None.

        Returns:
            None.
        """
        home_directory_path = os.path.dirname(os.getcwd())

        # Test case 1
        directory_path = check_directory_path_existence(home_directory_path, "logs")
        self.assertEqual(directory_path, "{}/logs".format(home_directory_path))

        # Test case 2
        directory_path = check_directory_path_existence(home_directory_path, "results")
        self.assertEqual(directory_path, "{}/results".format(home_directory_path))


if __name__ == '__main__':
    unittest.main()
 