from enum import Enum
from typing import List, Tuple, Any


class ChoosableEnum(Enum):
    """Enum class that can be directly exposed as choices for choosable parameters."""

    @classmethod
    def choice(cls) -> List[Tuple[str, Any]]:
        return [(choice.value, choice.name) for choice in cls]

    @classmethod
    def values(cls) -> List[Any]:
        return [value.value for value in cls]
