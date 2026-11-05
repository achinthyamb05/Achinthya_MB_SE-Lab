import pytest
from hypothesis import given, strategies as st
from food_delivery import parse_order, delivery_eta, coupon_discount


@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        parse_order(s)
    except (ValueError, TypeError):
        # Acceptable validation errors
        pass
    except Exception as e:
        pytest.fail(f"parse_order crashed unexpectedly with: {type(e).__name__}: {e}")


@given(st.text() | st.none())
def test_delivery_eta_no_crash(s):
    try:
        delivery_eta(s)
    except (ValueError, TypeError):
        # Acceptable validation errors
        pass
    except Exception as e:
        pytest.fail(f"delivery_eta crashed unexpectedly with: {type(e).__name__}: {e}")


@given(st.text() | st.none())
def test_coupon_discount_no_crash(s):
    try:
        coupon_discount(s)
    except (ValueError, TypeError):
        # Acceptable validation errors
        pass
    except Exception as e:
        pytest.fail(f"coupon_discount crashed unexpectedly with: {type(e).__name__}: {e}")