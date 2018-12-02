from pathlib import Path

from src.libs import aoc_utils


class SendingError(Exception):
    pass


class Problem:

    def __init__(self):
        self._input_file = None

    @property
    def problem(self) -> int:
        raise NotImplementedError

    @property
    def day(self) -> int:
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def get_data(self) -> Path:
        self._input_file = aoc_utils.get_data(day=self.day)
        return self._input_file


class ProblemRunner:

    def __init__(self, problem: Problem):
        self._problem = problem
        self._result = None

    def send(self):
        if not self._result:
            raise SendingError('Result is not ready.')
        aoc_utils.submit(
            answer=self._result,
            day=self._problem.day,
            level=self._problem.problem
        )

    def solve(self):
        self._problem.get_data()
        result = self._problem.run()
        self._result = str(result)
        return self._result
