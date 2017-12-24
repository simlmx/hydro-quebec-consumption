from utils import get_winter

def test_get_winter():
    assert get_winter('2017-10-12') == 2018
    assert get_winter('2017-11-12') == 2018
    assert get_winter('2017-12-12') == 2018
    assert get_winter('2018-01-01') == 2018
    assert get_winter('2018-02-01') == 2018
