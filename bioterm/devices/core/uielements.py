import re
from dataclasses import dataclass
from typing import Type


@dataclass
class UIElement:
    name: str
    id: str


@dataclass
class IntegerInput(UIElement):
    minValue: int
    maxValue: int
    increment: int
    return_type: Type[int] = int


@dataclass
class FloatInput(UIElement):
    minValue: float
    maxValue: float
    increment: float
    return_type: Type[float] = float


@dataclass
class TextInput(UIElement):
    regex: str
    return_type: Type[str] = str

    def __post_init__(self):
        if not self.is_valid_regex():
            raise ValueError(
                f"The regex '{self.regex}' is not a valid regular expression."
            )

    def is_valid_regex(self):
        """
        Verifies if the regex attribute is a valid regular expression.

        :return: True if the regex is valid, False otherwise.
        :rtype: bool
        """
        try:
            re.compile(self.regex)
            return True
        except re.error:
            return False


@dataclass
class EnumInput(UIElement):
    options: list
    return_type: Type[str] = str
