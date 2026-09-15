import pytest
from main import purchase_item

run_cases = [
    (10.00, 20.00, 10.00, None),
    (30.00, 20.00, None, "not enough gold"),
]

submit_cases = [
    pytest.param(15.10, 15.10, 0.00, None, marks=pytest.mark.submit),
    pytest.param(1430.00, 69.00, None, "not enough gold", marks=pytest.mark.submit),
    pytest.param(7.50, 7.50, 0.00, None, marks=pytest.mark.submit),
    pytest.param(100.00, 99.99, None, "not enough gold", marks=pytest.mark.submit),
    pytest.param(0.00, 0.00, 0.00, None, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("price", "gold_available", "expected", "expected_error"),
    run_cases + submit_cases,
)
def test_purchase_item(price, gold_available, expected, expected_error):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * price: {price:.2f}")
    print(f" * gold_available: {gold_available:.2f}")
    if expected_error is not None:
        with pytest.raises(Exception) as error:
            purchase_item(price, gold_available)
        print(f"Expected Exception: {expected_error}")
        print(f"  Actual Exception: {error.value!s}")
        assert str(error.value) == expected_error
        return
    result = purchase_item(price, gold_available)
    print(f"Expected: {expected:.2f}")
    print(f"  Actual: {result:.2f}")
    assert result == expected
