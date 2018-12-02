from collections import Counter
from dataclasses import dataclass, field

from src.libs.problem import Problem


@dataclass(unsafe_hash=True)
class ID:

    value: str
    counter: Counter = field(
        init=False, repr=False, compare=False, default=None)

    def repeated(self, occurrences) -> bool:
        if not self.counter:
            self.counter = Counter(self.value)
        return any(map(lambda x: x[1] == occurrences, self.counter.items()))


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
