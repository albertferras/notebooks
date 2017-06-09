from unittest.mock import NonCallableMock, Mock, MagicMock
import itertools

mock_methods_and_attributes = set(itertools.chain(*(dir(klass) for klass in (Mock, MagicMock, NonCallableMock))))


def get_non_mock_attributes(mock):
    return [attr for attr in dir(mock)
            if attr not in mock_methods_and_attributes
            and attr != 'method_calls']
