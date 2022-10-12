from typing import Callable, Final

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from benchmark_task.main import (
    make_something_with_len,
    make_something_with_count,
    make_something_with_count_2,
    make_something_with_len_2,
)

AMOUNT: Final[int] = 100000


@pytest.mark.parametrize(
    "func,amount",
    [
        (make_something_with_count, AMOUNT),
        (make_something_with_len, AMOUNT),
        (make_something_with_count_2, AMOUNT),
        (make_something_with_len_2, AMOUNT),
    ],
)
def test_benchmark_for_functions(func: Callable, amount: int, benchmark: BenchmarkFixture):
    result_ = benchmark(
        func,
        amount,
    )
    assert len(result_) == amount


# @pytest.mark.parametrize(
#     "func,amount",
#     [
#         (make_something_with_len, AMOUNT),
#         (make_something_with_count, AMOUNT),
#     ],
# )
# def test_for_functions(
#     func: Callable,
#     amount: int,
# ):
#     result_ = func(
#         amount=amount,
#     )
#     assert len(result_) == amount
