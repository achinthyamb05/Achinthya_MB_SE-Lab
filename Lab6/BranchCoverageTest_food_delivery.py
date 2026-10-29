import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


def test_delivery_charge_boundary_errors():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(-1, 200, False)
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(15.1, 200, False)


def test_delivery_charge_tiers_and_rain():
    assert delivery_charge(1, 500, False) == 0
    assert delivery_charge(1, 550, True) == 30
    assert delivery_charge(3, 400, False) == 20
    assert delivery_charge(3, 400, True) == 50
    assert delivery_charge(8, 400, False) == 40
    assert delivery_charge(8, 400, True) == 70
    assert delivery_charge(12, 400, False) == 60
    assert delivery_charge(15, 400, True) == 90


def test_apply_coupon_all_branches():
    assert apply_coupon(300, None, True) == 300
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID_CODE", True)
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)
    assert apply_coupon(400, "WELCOME", True) == 300
    assert apply_coupon(100, "SAVE50", True) == 100
    assert apply_coupon(300, "SAVE50", False) == 250


def test_estimated_time_all_branches():
    assert estimated_time(5, False, False) == 35
    assert estimated_time(5, True, False) == 45
    assert estimated_time(5, False, True) == 50
    assert estimated_time(5, True, True) == 65