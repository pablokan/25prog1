

from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class ImprovedInit:
    """
    A class demonstrating improved practices for an __init__ method.

    This class uses the @dataclass decorator to simplify creation, adds type
    hinting for clarity, provides meaningful default values, and includes
    validation logic.

    Attributes:
        name (str): The name of the object. Cannot be empty.
        configuration (dict): A configuration dictionary.
        items (list[Any]): A list of items.
        version (int): The version number.
    """
    name: str
    configuration: dict = field(default_factory=dict)
    items: list[Any] = field(default_factory=list)
    version: int = 1

    def __post_init__(self):
        """Post-initialization validation."""
        if not self.name:
            raise ValueError("The 'name' attribute cannot be empty.")


def main():
    print(f'Debugging ######## {1=} #########')
    

if __name__ == '__main__':
    main()