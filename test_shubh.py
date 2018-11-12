import shubh

def test_cal_add():
    total = shubh.addition(10,7)
    assert total == 17

def test_cal_sub():
    diff = shubh.difference(5,4)
    assert diff == 1


def test_cal_mul():
    prod = shubh.mul(7,3)
    assert prod == 21


def test_div():
    divition = shubh.div(30,5)
    assert divition == 6


def test_facto():
    factorial = shubh.fact(5)
    assert factorial == 120
