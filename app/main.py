from abc import ABC
from typing import Any


class IntegerRange:
    def __init__(self, min_amount: int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner, name):
        self.protected_name = "_" + name

    def __get__(self, instance, owner):
        value = getattr(instance, self.protected_name)
        return value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError
        if not (self.min_amount <= value <= self.max_amount):
            raise ValueError
        setattr(instance, self.protected_name, value)


class Visitor:
   def __init__(self, name: str, age: int, weight: int, height: int) -> None:
       self.name = name
       self.age = age
       self.weight = weight
       self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self, age: Any, weight: Any, height: Any) -> None  :
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    def __init__(self):
        super().__init__(IntegerRange(4, 14),
                         IntegerRange(80, 120),
                         IntegerRange(20, 50))


class AdultSlideLimitationValidator(SlideLimitationValidator):
    def __init__(self):
        super().__init__(IntegerRange(14, 60),
                         IntegerRange(120, 220),
                         IntegerRange(50, 120))


class Slide:
    def __init__(
        self,
        name: str,
        limitation_class: ChildrenSlideLimitationValidator | AdultSlideLimitationValidator
    ) -> None:
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, person: Visitor):
        if self.limitation_class == ChildrenSlideLimitationValidator:
            ChildrenSlideLimitationValidator(person.age, person.weight, person.height)
            return True
        if self.limitation_class == AdultSlideLimitationValidator:
            AdultSlideLimitationValidator(person.age, person.weight, person.height)
            return True
        return False
