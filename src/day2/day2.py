from collections import Counter
from dataclasses import dataclass, field
from typing import Set, Union

from src.libs.problem import Problem


@dataclass(frozen=True)
class CleanedID:
    value: str
    original: str = field(compare=False)


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
        for i in range(len(self.value)):
            val = self.value[:i] + self.value[i + 1:]
            elements.add(CleanedID(value=val, original=self.value))
        return elements


@dataclass
class DictDiffIDs:
    values: Set[CleanedID] = field(default_factory=set)

    def add(self, values: Set[CleanedID]) -> Union[CleanedID, None]:
        for val in values:
            if val in self.values:
                return val
            self.values.add(val)


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
                return find_repeated
