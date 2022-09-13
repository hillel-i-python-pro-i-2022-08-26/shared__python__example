import csv
import pathlib
import random
from typing import Final, NamedTuple

from faker import Faker

from settings.paths import FILES_PATH

fake = Faker()

KEY__NAME: Final[str] = "Name"
KEY__AGE: Final[str] = "Age"


def write_to_csv(path: pathlib.Path, items_amount: int = 10):
    with open(path, mode="w", newline="") as csvfile:
        fieldnames = [KEY__NAME, KEY__AGE]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for _ in range(items_amount):
            writer.writerow({KEY__NAME: fake.first_name(), KEY__AGE: random.randint(10, 90)})


class Human(NamedTuple):
    name: str
    age: int
    something: None = None


def read_from_csv(path: pathlib.Path) -> list:
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        items = [Human(name=row[KEY__NAME], age=int(row[KEY__AGE])) for row in reader]
    return items


def main():
    path_to_csv = FILES_PATH.joinpath("my.csv")

    path_to_csv.unlink(missing_ok=True)

    write_to_csv(path=path_to_csv)

    humans = read_from_csv(path=path_to_csv)  # noqa: F841

    print()


if __name__ == "__main__":
    main()
