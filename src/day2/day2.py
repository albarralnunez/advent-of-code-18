from collections import Counter
from copy import copy
from dataclasses import dataclass, field
from typing import Set, Union, Dict

from src.libs.problem import Problem


@dataclass(frozen=True)
class RepeatedID:
    value: str
    original: str


@dataclass(unsafe_hash=True)
class ID:

    value: str
    counter: Counter = field(
        init=False, repr=False, compare=False, default=None)

    def repeated(self, occurrences) -> bool:
        if not self.counter:
            self.counter = Counter(self.value)
        return any(map(lambda x: x[1] == occurrences, self.counter.items()))

    def different_elements(self):
        elements = set()
        enum_value = list(enumerate(self.value))
        for i, x in enum_value:
            val = copy(enum_value)
            del val[i]
            original = self.value[:i] + self.value[i + 1:]
            final_value = set(val)
            elements.add(RepeatedID(value=str(final_value), original=original))
        return elements


@dataclass
class DictDiffIDs:

    values: Dict[str, str] = field(default_factory=dict)

    def add(self, values: Set[RepeatedID]) -> Union[RepeatedID, None]:
        for val in values:
            if val.value in self.values:
                return val
            self.values[val.value] = val.original


class Day2Problem1(Problem):
    day = 2
    problem = 1

    def run(self):
        with self._input_file.open() as f:
            ids = [ID(x) for x in f.readlines()]
        repeated_two = filter(lambda x: x, map(lambda x: x.repeated(2), ids))
        repeated_three = filter(lambda x: x, map(lambda x: x.repeated(3), ids))
        result = len(list(repeated_two)) * len(list(repeated_three))
        return result


class Day2Problem2(Problem):
    day = 2
    problem = 2

    def run(self):
        with self._input_file.open() as f:
            ids = [ID(x.strip()) for x in f.readlines()]
        id_dict = DictDiffIDs()
        for id_value in ids:
            find_repeated = id_dict.add(id_value.different_elements())
            if find_repeated:
                return find_repeated.original

