from abc import ABC, abstractmethod
from typing import Protocol


class Heart:
    ...


class Human:
    def __init__(self):
        self.heart = Heart()


class Table:
    ...


class Chair:
    ...


class Room:
    def __init__(self, *items):
        self._furniture: list[Table | Chair] = [
            *items,
        ]

    def add_furniture(self, item):
        self._furniture.append(item)


class Engine:
    ...


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine


# ---------
# class MegaLegacy:
#     def method_1(self):
#         ...
#     def method_2(self):
#         ...
#     def method_3(self):
#         ...
#     def method_4(self):
#         ...
#     def method_5(self):
#         ...


class LegacyProtocol(Protocol):
    @property
    @abstractmethod
    def field_1(self) -> str:
        ...

    @property
    @abstractmethod
    def field_2(self) -> int:
        ...

    @field_2.setter
    @abstractmethod
    def field_2(self, value: int):
        ...
        # self._field_2 = value


# LegacyProtocol
class LegacyMixin1:
    def method_1(self):
        ...

    def method_2(self):
        ...


class LegacyMixin2:
    def method_3(self):
        ...


class AbstractLegacy(ABC):
    @abstractmethod
    def method_1(self):
        """
        Make me happy.
        :return:
        """
        ...

    @abstractmethod
    def method_2(self):
        ...

    @abstractmethod
    def method_3(self):
        ...

    @abstractmethod
    def method_4(self):
        ...

    @abstractmethod
    def method_5(self):
        ...


class MegaLegacy(LegacyMixin1, LegacyMixin2, AbstractLegacy):
    def method_4(self):
        ...

    def method_5(self):
        ...


# -----


class Feature1:
    def method_1(self):
        ...

    def method_2(self):
        ...


class Feature2:
    def method_3(self):
        ...


class Modern:
    def __init__(self):
        self.feature_1 = Feature1()
        self.feature_2 = Feature2()

    def method_4(self):
        ...

    def method_5(self):
        ...

    def method_1(self):
        self.feature_1.method_1()


modern = Modern()

# modern.feature_1.method_1()
modern.method_1()
