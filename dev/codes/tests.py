# authors_name = 'Preetham Ganesh'
# project_title = 'Comparison of Approaches towards Classification of Birds Species'
# email = 'preetham.ganesh2021@gmail.com'


import os

import pytest

from utils import check_directory_path_existence


def test_check_directory_path_existence() -> None:
    """Tests check_directory_path_existence function from utils.py with multiple test cases.

    Args:
        None.

    Returns:
        None.
    """
    home_directory_path = os.path.dirname(os.getcwd())

    # Test case 1
    directory_path = check_directory_path_existence(home_directory_path, "logs")
    assert directory_path, "{}/logs".format(home_directory_path)

    # Test case 2
    directory_path = check_directory_path_existence(home_directory_path, "results")
    assert directory_path, "{}/results".format(home_directory_path)
