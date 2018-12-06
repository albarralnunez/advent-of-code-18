import re

from src.day3.models import Position, Area, Claim, Fabric, CounterMultipleClaims, SingleClaimFinder, ClaimID
from src.libs.problem import Problem


class Day3Problem(Problem):

    line_regex = re.compile(
        r"^#(?P<identifier>\d+) @ (?P<point_x>\d+),(?P<point_y>\d+): (?P<width>\d+)x(?P<height>\d+)$"
    )

    @property
    def solver_class(self):
        raise NotImplementedError

    def _parse_line(self, line):
        matched_line = self.line_regex.match(line)
        return Claim(
            identifier=ClaimID(int(matched_line.group('identifier'))),
            area=Area(
                starting_point=Position(
                    int(matched_line.group('point_x')),
                    int(matched_line.group('point_y'))
                ),
                width=int(matched_line.group('width')),
                height=int(matched_line.group('height'))
            )
        )

    def _parse_input(self, f):
        lines = (x.strip() for x in f.readlines())
        return map(self._parse_line, lines)

    def run(self):
        fabric = Fabric()
        input_file = self.get_data()
        with input_file.open() as f:
            claims = self._parse_input(f)
            fabric.make_claims(claims)
        solver = self.solver_class(fabric)
        result = solver()
        return result


class Day3Problem1(Day3Problem):
    day = 3
    problem = 1
    solver_class = CounterMultipleClaims


class Day3Problem2(Day3Problem):
    day = 3
    problem = 2
    solver_class = SingleClaimFinder
