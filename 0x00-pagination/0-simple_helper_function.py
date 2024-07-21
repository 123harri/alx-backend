#!/usr/bin/env python3
"""
This module provides a helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Parameters:
    - page: Current page number (1-indexed)
    - page_size: Number of items per page

    Returns:
    - A tuple containing the start index and the end
    index for the given pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
