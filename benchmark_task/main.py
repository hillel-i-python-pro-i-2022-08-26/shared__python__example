from random import randint
from typing import Iterator, Protocol, TypeAlias, NamedTuple, Any

from faker import Faker

fake = Faker()

T_LOGIN: TypeAlias = str
T_PASSWORD: TypeAlias = str


class UserProtocol(Protocol):
    login: T_LOGIN
    password: T_PASSWORD


class User(NamedTuple):
    login: T_LOGIN
    password: T_PASSWORD


def validate(users: list[UserProtocol], amount: int) -> None:
    logins = set(map(lambda user: user.login, users))
    if amount != (amount_of_logins := len(logins)):
        raise ValueError(f'Not enough of unique items. Required: "{amount}". Provided: "{amount_of_logins}"')


def generate_user_name(amount):
    return f"{fake.user_name() + str(randint(0, amount))}"


def generate_password():
    return fake.password(length=randint(5, 25), special_chars=False)


def make_something_with_count(amount: int) -> Any:
    count_generation = 1

    dict_users_data = {}
    while len(dict_users_data) < amount:
        user_name = generate_user_name(amount)
        user_password = generate_password()
        if user_name in dict_users_data:
            continue
        # print(f'Generation ==> {count_generation}')
        count_generation += 1
        dict_users_data[user_name] = user_password
    return dict_users_data


def _make_something_with_count_2(amount: int) -> Any:
    dict_users_data = {}
    while len(dict_users_data) < amount:
        user_name = generate_user_name(amount)
        if user_name in dict_users_data:
            continue

        user_password = generate_password()
        dict_users_data[user_name] = user_password
        yield User(
            login=user_name,
            password=user_password,
        )


def make_something_with_count_2(amount: int) -> Any:
    return list(_make_something_with_count_2(amount=amount))


def generate_users(amount: int) -> Iterator[UserProtocol]:
    logins = set()

    while len(logins) < amount:
        login = generate_user_name(amount=amount)

        if login in logins:
            continue

        logins.add(login)
        yield User(
            login=login,
            password=generate_password(),
        )


def make_something_with_len(amount: int) -> Any:
    return list(generate_users(amount=amount))


def generate_users_2(amount: int) -> Iterator[UserProtocol]:
    logins = []

    while len(logins) < amount:
        login = generate_user_name(amount=amount)

        if login in logins:
            continue

        logins.append(login)
        yield User(
            login=login,
            password=generate_password(),
        )


def make_something_with_len_2(amount: int) -> Any:
    return list(generate_users_2(amount=amount))


if __name__ == "__main__":
    make_something_with_len_2(amount=1000)
