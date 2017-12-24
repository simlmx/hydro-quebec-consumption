import pytest
from data_loading import load_csv_file, load_csv_files

TEST_FILE = 'tests/daily_data_fixture.csv'
TEST_FILE2 = 'tests/daily_data_fixture2.csv'

def test_load_csv_file():
    data = load_csv_file(TEST_FILE)
    assert data == {
        '2017-12-22': {'kwh': 81.07, 'temp': -13},
        '2017-12-21': {'kwh': 67.56, 'temp': -13},
    }

def test_load_csv_files():

    with pytest.raises(ValueError):
        data = load_csv_files(TEST_FILE, TEST_FILE)

    data = load_csv_file(TEST_FILE)
    assert data == {
        '2017-12-22': {'kwh': 81.07, 'temp': -13},
        '2017-12-21': {'kwh': 67.56, 'temp': -13},
    }

    data = load_csv_files(TEST_FILE, TEST_FILE2)
    assert data == {
        '2017-12-22': {'kwh': 81.07, 'temp': -13},
        '2017-12-21': {'kwh': 67.56, 'temp': -13},
        '2017-12-19': {'kwh': 2, 'temp': 4},
        '2017-12-20': {'kwh': 1, 'temp': 3},
    }
