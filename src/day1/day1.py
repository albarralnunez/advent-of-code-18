from src.day1.frequency_counter import FrequencyCounter, FirstFrequencyMatch
from src.day1.input_parser import InputParser
from src.day1.line_parser import LineParser
from src.libs.problem import Problem


class Day1Problem(Problem):

    @property
    def frequency_counter(self):
        raise NotImplementedError

    def run(self):
        frequency_counter = self.frequency_counter()
        with self._input_file.open() as f:
            input_parser = InputParser(f, LineParser)
            instructions = input_parser.parse()
            result = frequency_counter.apply(*instructions)
        return result


class Day1Problem1(Day1Problem):
    problem = 1
    day = 1
    frequency_counter = FrequencyCounter


class Day1Problem2(Day1Problem):
    problem = 2
    day = 1
    frequency_counter = FirstFrequencyMatch
