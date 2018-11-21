import pytest
import shubh


@pytest.mark.parametrize("input1, input2, output",
                          [
                              (10,7,17),
                              (15,8,23),
                              (2,4,6),
                              (4,5,9),
                              (66,2,70)
                            ]
                          )
def test_add(input1, input2, output):
    assert output == shubh.addition(input1, input2)
