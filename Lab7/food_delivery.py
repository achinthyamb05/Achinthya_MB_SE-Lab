import math
import re


def parse_order(items_csv):
    if not isinstance(items_csv, str):
        raise TypeError("items_csv must be a string")

    order = {}
    cleaned = items_csv.strip()
    if not cleaned:
        return order

    for item in cleaned.split(','):
        item = item.strip()
        if not item:
            continue
        parts = item.split(':')
        if len(parts) != 2:
            raise ValueError(f"Invalid item format: '{item}'")

        name, qty_str = parts[0].strip(), parts[1].strip()
        if not name:
            raise ValueError("Item name cannot be empty")

        try:
            qty = int(qty_str)
            if qty <= 0:
                raise ValueError("Quantity must be positive")
        except ValueError:
            raise ValueError(f"Invalid quantity: '{qty_str}'")

        order[name] = order.get(name, 0) + qty

    return order


def delivery_eta(distance_km):
    if distance_km is None:
        raise TypeError("Distance cannot be None")

    try:
        dist = float(distance_km)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid distance value: '{distance_km}'")

    if math.isnan(dist) or math.isinf(dist):
        raise ValueError("Distance must be a finite number")

    if dist < 0:
        raise ValueError("Distance cannot be negative")

    return int(15 + dist * 4)


def coupon_discount(code):
    if not isinstance(code, str):
        raise TypeError("Coupon code must be a string")

    clean_code = code.strip().upper()
    match = re.match(r"^SAVE(\d+)$", clean_code)
    if not match:
        raise ValueError(f"Invalid coupon code format: '{code}'")

    return int(match.group(1))


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    try:
        result = parse_order(user_input)
        print("Order:", result)
    except Exception as e:
        print(f"Error: {e}")

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    try:
        result = delivery_eta(user_input)
        print("ETA in Minutes:", result)
    except Exception as e:
        print(f"Error: {e}")

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    try:
        result = coupon_discount(user_input)
        print("Discount:", result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()