import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


def test_delivery_charge_out_of_range():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 100, False)
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(16, 100, False)


def test_delivery_charge_free_delivery():
    assert delivery_charge(5, 500, False) == 0
    assert delivery_charge(5, 600, True) == 30


def test_delivery_charge_distance_tiers():
    assert delivery_charge(2, 200, False) == 20
    assert delivery_charge(5, 200, False) == 40
    assert delivery_charge(10, 200, False) == 60


def test_apply_coupon():
    assert apply_coupon(300, None, False) == 300
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID", False)
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)
    assert apply_coupon(150, "SAVE50", True) == 150
    assert apply_coupon(300, "SAVE50", False) == 250


def test_estimated_time():
    assert estimated_time(5, False, False) == 35
    assert estimated_time(5, True, False) == 45
    assert estimated_time(5, True, True) == 65