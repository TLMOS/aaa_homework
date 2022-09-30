from unittest import mock
import pytest

from what_is_year_now import what_is_year_now, API_URL

FORMAT_YEAR_IS_FIRST = 0
FORMAT_YEAR_IS_LAST = 1
FORMAT_INVALID = 2


class MockedOutputStream:
    def __init__(self, msg):
        self.msg = msg

    def read(self):
        return self.msg


def get_mocked_url_open(url, date_format: bool):
    class MockedURLOpen():
        def __init__(self, url):
            self.url = url

        def __enter__(self):
            if self.url == url:
                if date_format == FORMAT_YEAR_IS_FIRST:
                    return MockedOutputStream(
                        '{"currentDateTime": "2019-03-01"}')
                elif date_format == FORMAT_YEAR_IS_LAST:
                    return MockedOutputStream(
                        '{"currentDateTime": "01.03.2019"}')
                elif date_format == FORMAT_INVALID:
                    return MockedOutputStream(
                        '{"currentDateTime": "Invalid Date"}')

        def __exit__(self, exc_type, exc_value, traceback):
            return True
    return MockedURLOpen


@mock.patch('urllib.request.urlopen',
            side_effect=get_mocked_url_open(API_URL, FORMAT_YEAR_IS_FIRST))
def test_year_is_first(mocked_url_open):
    assert what_is_year_now() == 2019


@mock.patch('urllib.request.urlopen',
            side_effect=get_mocked_url_open(API_URL, FORMAT_YEAR_IS_LAST))
def test_year_is_last(mocked_url_open):
    assert what_is_year_now() == 2019


@mock.patch('urllib.request.urlopen',
            side_effect=get_mocked_url_open(API_URL, FORMAT_INVALID))
def test_invalid_date(mocked_url_open):
    with pytest.raises(ValueError):
        what_is_year_now()
