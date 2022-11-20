"""Stores custom exceptions"""


class IncorrectLocationException(Exception):
    """Raised when location can not be found using the query"""
    def __init__(self, *args, msg='Location can not be found using the query.'):
        super().__init__(*args, msg)


class DatasetDirectoryEmpty(Exception):
    """Raised when there are no datasets"""
    def __init__(self, *args, msg='No datasets found in the datasets directory.'):
        super().__init__(*args, msg)
