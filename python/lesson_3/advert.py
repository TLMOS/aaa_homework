from keyword import iskeyword
from typing import Any, Mapping, Sequence


class ColorizeMixin:
    """Mixin for colorizing __repr__ magic method"""

    def __str__(self):
        return f'\033[0;{self.repr_color_code}m{self.__repr__()}\033[0m'


class FromMapping:
    """Class for converting from a mapping to a python object"""

    @staticmethod
    def __is_correct_mapping(mapping: Mapping) -> bool:
        """Check if all mapping keys are strings"""
        return all(map(lambda x: isinstance(x, str), mapping.keys()))

    def __init__(self, mapping: Mapping[str, Any]):
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, Mapping) and self.__is_correct_mapping(value):
                value = FromMapping(value)
            if isinstance(value, Sequence):
                for i, x in enumerate(value):
                    if isinstance(x, Mapping) and self.__is_correct_mapping(x):
                        value[i] = FromMapping(x)
            setattr(self, key, value)


class Advert(ColorizeMixin):
    """Advert class defined by homework task"""

    repr_color_code = 32  # Default color code (Green)

    def __init__(self, mapping: Mapping[str, Any]):
        self.__price = 0
        for key, value in vars(FromMapping(mapping)).items():
            setattr(self, key, value)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price must be positive")
        self.__price = value
