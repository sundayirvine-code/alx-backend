#!/usr/bin/env python3

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

