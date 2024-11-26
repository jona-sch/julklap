from dataclasses import dataclass, field
from itertools import permutations
from typing import List, Set, Tuple
import random

from julklap.person import Person
from julklap.exceptions import NoPossibleJulklapMappingError


@dataclass
class Group:
    """
    Represents a group of people.
    """

    people: Set[Person] = field(default_factory=set)
    """People in the group."""

    exclusions: List[Tuple[Person, Person]] = field(default_factory=list)
    """Exclusions in the group: two persons in a same tuple can't buy each other gifts."""

    name: str = field(default="People Group")
    """Name of the group."""

    @property
    def number_of_people(self) -> int:
        return len(self.people)

    def add_person(self, person: Person) -> None:
        """
        Add a person to the people of the group.

        Args:
            person (Person): person to add.
        """
        self.people.add(person)

    def _validate_shuffled_people(self, shuffled_people: List[Person]) -> bool:
        """
        Validate a shuffled people list with the desired exclusions. If it's possible to create a Julklap
        combination, returns True, else returns False.

        Args:
            shuffled_people (List[Person]): list of all the people that has been shuffled randomly.

        Returns:
            bool
        """
        if not self.exclusions:
            return True
        for i in range(len(shuffled_people) - 1):
            for excluded_person_1, excluded_person_2 in self.exclusions:
                if {excluded_person_1, excluded_person_2} == {
                    shuffled_people[i],
                    shuffled_people[i + 1],
                }:
                    return False
        for excluded_person_1, excluded_person_2 in self.exclusions:
            if {excluded_person_1, excluded_person_2} == {
                shuffled_people[0],
                shuffled_people[-1],
            }:
                return False
        return True

    def _create_matches_with_exclusion_brute_force(self) -> List[Tuple[Person]]:
        """
        Create matches between people of the group when there are no exclusions.

        Returns:
            List[Tuple[Person]]: Each tuple represents a "gift link" tuple[0] -> tuple[1].

        Raises:
            NoPossibleJulklapMappingError: if it isn't possible to find a Julklap combination.
        """
        for shuffled_people in permutations(self.people):
            if self._validate_shuffled_people(shuffled_people):
                matches: List[Tuple[Person]] = []
                for i in range(len(self.people) - 1):
                    matches.append((shuffled_people[i], shuffled_people[i + 1]))
                matches.append((shuffled_people[-1], shuffled_people[0]))
                return matches
        raise NoPossibleJulklapMappingError(
            f"Exclusions prevent creation of a Julklap combination: exclusions={self.exclusions}, people={self.people}"
        )

    def create_matches(self) -> List[Tuple[Person]]:
        """
        Create matches between people of the group.

        Returns:
            List[Tuple[Person]]: Each tuple represents a "gift link" tuple[0] -> tuple[1].

        Raises:
            NoPossibleJulklapMappingError: if it isn't possible to find a Julklap combination.
        """
        if len(self.people) < 2:
            raise NoPossibleJulklapMappingError(
                f"You need at least 2 people to create matches. You have {len(self.people)}."
            )
        return self._create_matches_with_exclusion_brute_force()
