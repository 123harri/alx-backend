#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict:
        """
        Get a page from the dataset with hypermedia metadata, resilient to
        deletions.

        Parameters:
        - index: Start index for the page
        - page_size: Number of items per page

        Returns:
        - A dictionary containing hypermedia metadata
        """
        assert index is not None
        assert isinstance(index, int)
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        keys = sorted(dataset.keys())

        if index not in keys:
            valid_keys = [k for k in keys if k >= index]
            if not valid_keys:
                return {
                    'index': index,
                    'next_index': None,
                    'page_size': page_size,
                    'data': []
                }
            index = valid_keys[0]

        start_index = keys.index(index)
        data = [dataset[k] for k in keys[start_index:start_index + page_size]]

        next_index = None
        if start_index + page_size < len(keys):
            next_index = keys[start_index + page_size]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
