from src.app.math import Math

def test_sum():
    math = Math()
    assert math.sum(1, 1) == 2