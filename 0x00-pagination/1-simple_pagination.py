#!/usr/bin/env python3
"""Simple pagination sample.
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Calculate the start and end indexes corresponding to the range of items to be displayed on a specific page.

    Args:
        page (int): The page number (1-indexed) for which to calculate the range.
        page_size (int): The number of items to show on each page.

    Returns:
        tuple: A tuple of size two containing the start index and end index of the item range.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """
        Get the specified page of the dataset.

        Args:
            page (int, optional): The page number (1-indexed) for which to retrieve the data.
            page_size (int, optional): The number of items to show on each page.

        Returns:
            List[List]: The list of rows corresponding to the specified page of the dataset.
        """
        assert isinstance(page, int) and page > 0, "Page number must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index+1]
