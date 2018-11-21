import pytest
import shubh
import sys

@pytest.mark.mac
def test_add():
    total = shubh.addition(10,7)
    assert total == 17

@pytest.mark.windows
@pytest.mark.skipif(sys.version_info > (3,0), reason = " You have an advanced python version!")
def test_cal_sub():
    diff = shubh.difference(5,4)
    assert diff == 1

def test_cal_mul():
    prod = shubh.mul(7,3)
    assert prod == 21

@pytest.mark.windows
def test_div():
    divition = shubh.div(30,5)
    assert divition == 6


@pytest.mark.windows
def test_windoes_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True
