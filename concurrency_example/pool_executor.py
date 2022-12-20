import concurrent.futures
import logging
import random
from collections.abc import Iterator
from math import ceil, floor
from typing import NamedTuple, Final

from requests_example.init_logging import init_logging


class ActionArgs(NamedTuple):
    alphabet: str
    number_of_start_word: int
    word_length: int


def make_action_partial(alphabet: str, number_of_start_word: int, word_length: int) -> int:
    logger = logging.getLogger(__name__)
    logger.info(f"{alphabet=}, {number_of_start_word=}")

    start_word = [alphabet[0] for _ in range(word_length)]  # noqa: F841

    return number_of_start_word


def make_action__wrapper(args: ActionArgs) -> int:
    logger = logging.getLogger(__name__)
    logger.info(f"{args=}")

    return make_action_partial(**args._asdict())


def main():
    alphabet = "abc"
    word_length = 5

    total_number_of_words = len(alphabet) ** word_length

    items_in_package_amount = 10

    packages_amount = ceil(total_number_of_words / items_in_package_amount)

    logger = logging.getLogger(__name__)
    logger.info(f"{alphabet=}, {word_length=}, {total_number_of_words=}")

    packages = [
        ActionArgs(
            alphabet=alphabet,
            number_of_start_word=items_in_package_amount * package_number,
            word_length=word_length,
        )
        for package_number in range(packages_amount)
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(
            make_action__wrapper,
            packages,
        )

    print(list(results))


def convert_decimal_number_to_custom_base(number: int, base: int) -> Iterator[int]:
    """Convert decimal integer to list of numbers for custom base by iteration. From lowest to bigger."""
    number_to_convert = number
    while number_to_convert:
        floor_division, remainder = divmod(number_to_convert, base)
        yield remainder

        number_to_convert = floor_division


def main_2():
    alphabet = "abc"
    alphabet_length = len(alphabet)
    word_length = 5

    min_character_index: Final[int] = 0
    max_character_index: Final[int] = alphabet_length - 1

    total_number_of_words: Final[int] = len(alphabet) ** word_length
    # -----
    number_of_start_word = floor(total_number_of_words / 2)

    number_in_decimal_system = number_of_start_word
    number_in_alphabet_length_system_as_list = list(
        convert_decimal_number_to_custom_base(number=number_in_decimal_system, base=alphabet_length)
    )

    # start_word_as_digits = [0 for _ in range(word_length)]
    start_word_as_digits = number_in_alphabet_length_system_as_list

    start_word_as_digits = [random.randint(min_character_index, max_character_index) for _ in range(word_length)]

    word = "".join([alphabet[character_index] for character_index in start_word_as_digits])  # noqa: F841

    # start_word = [alphabet[0 * word_length] for _ in range(word_length)]

    print()


if __name__ == "__main__":
    init_logging()
    # main()
    main_2()
