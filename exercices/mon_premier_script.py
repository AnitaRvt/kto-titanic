########### EXERCICE ##########
from dataclasses import dataclass
from typing import List

MINIMUM_LETTERS_THRESHOLD: int = 7


@dataclass
class FirstName:
    value: str


def count_first_names_longer_than_threshold(
    first_names: List[FirstName],
) -> int:
    return sum(
        1
        for first_name in first_names
        if len(first_name.value) > MINIMUM_LETTERS_THRESHOLD
    )


import unittest
from mon_premier_script import (
    count_first_names_longer_than_threshold,
    FirstName,
)


class TestCountFirstNamesLongerThanThreshold(unittest.TestCase):

    def test_count_first_names(self) -> None:
        first_names = [
            FirstName("Guillaume"),
            FirstName("Gilles"),
            FirstName("Juliette"),
            FirstName("Antoine"),
            FirstName("François"),
            FirstName("Cassandre"),
        ]

        result: int = count_first_names_longer_than_threshold(
            first_names=first_names
        )

        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()