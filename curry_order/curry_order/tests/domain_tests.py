from typing import (
    Dict,
    List,
    Tuple,
)

import pytest

import curry_order.domains


def test_order_sum():
    cacher = curry_order.domains.Cacher()
    chiken_order = curry_order.domains.RecieptItem(curry_order.domains.Item.chiken_curry, 1)
    beef_order = curry_order.domains.RecieptItem(curry_order.domains.Item.beef_curry, 2)

    expect = (
        [
            (chiken_order, 700),
            (beef_order, 1800)
        ],
        2500)
    
    assert cacher.order_sum([chiken_order, beef_order]) == expect
