import pytest
from main import parse_filter, apply_filter, parse_agg, apply_agg


@pytest.fixture
def test_data():
    return [
        {"name": "iphone 15 pro",
         "brand": "apple",
         "price": "999",
         "rating": "4.9"},
        {"name": "galaxy s23 ultra",
         "brand": "samsung",
         "price": "1199",
         "rating": "4.8"},
        {"name": "redmi note 12",
         "brand": "xiaomi",
         "price": "199",
         "rating": "4.6"},
        {"name": "poco x5 pro",
         "brand": "xiaomi",
         "price": "299",
         "rating": "4.4"},
    ]


def test_parse_filter_numeric():
    field, op_func, value = parse_filter('price>500')
    assert field == 'price'
    assert value == '500'
    assert op_func(600, 500)
    assert not op_func(400, 500)


def test_parse_filter_text():
    field, op_func, value = parse_filter('brand=xiaomi')
    assert field == 'brand'
    assert value == 'xiaomi'
    assert op_func('xiaomi', 'xiaomi')
    assert not op_func('apple', 'xiaomi')


def test_apply_filter_numeric(test_data):
    filtered = apply_filter(test_data, "price", lambda a, b: a > b, "500")
    assert len(filtered) == 2
    assert all(float(item["price"]) > 500 for item in filtered)


def test_apply_filter_text(test_data):
    filtered = apply_filter(test_data, "brand", lambda a, b: a == b, "xiaomi")
    assert len(filtered) == 2
    assert all(item["brand"] == "xiaomi" for item in filtered)


def test_parse_agg_avg():
    column, agg_func = parse_agg("price=avg")
    assert column == "price"
    assert agg_func([10, 20, 30]) == 20


def test_parse_agg_min():
    column, agg_func = parse_agg("price=min")
    assert column == "price"
    assert agg_func([10, 20, 30]) == 10


def test_parse_agg_max():
    column, agg_func = parse_agg("price=max")
    assert column == "price"
    assert agg_func([10, 20, 30]) == 30


def test_apply_agg_avg(sample_data):
    result = apply_agg(sample_data, "price",
                       lambda nums: sum(nums) / len(nums))
    expected = (999 + 1199 + 199 + 299) / 4
    assert abs(result - expected) < 1e-6


def test_apply_agg_min(sample_data):
    result = apply_agg(sample_data, "price", min)
    assert result == 199


def test_apply_agg_max(sample_data):
    result = apply_agg(sample_data, "price", max)
    assert result == 1199
