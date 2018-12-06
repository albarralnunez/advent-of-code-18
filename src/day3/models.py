from dataclasses import dataclass, field
from itertools import dropwhile
from typing import Dict, Iterable, Set


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class Area:
    starting_point: Position
    width: int
    height: int

    def get_all_tails(self):
        x_positions_end = self.starting_point.x + self.width
        y_positions_end = self.starting_point.y + self.height
        x_positions = range(self.starting_point.x, x_positions_end)
        y_positions = range(self.starting_point.y, y_positions_end)
        return (Position(x_position, y_position) for x_position in x_positions for y_position in y_positions)


@dataclass(frozen=True)
class ClaimID:
    value: int


@dataclass(frozen=True)
class Claim:
    identifier: ClaimID
    area: Area


@dataclass(frozen=True)
class Fabric:
    space: Dict[Position, Set[ClaimID]] = field(default_factory=dict)

    @property
    def space_claims(self):
        return self.space.values()

    def make_claim(self, claim: Claim):
        for position in claim.area.get_all_tails():
            if position in self.space:
                self.space[position].add(claim.identifier)
            else:
                self.space[position] = {claim.identifier}

    def make_claims(self, claims: Iterable[Claim]):
        for claim in claims:
            self.make_claim(claim)


@dataclass(frozen=True)
class Solver:
    fabric: Fabric

    def __call__(self):
        raise NotImplementedError


class SingleClaimFinder(Solver):

    def __call__(self):
        find_first_single_claim = dropwhile(lambda x: len(x) > 1, self.fabric.space_claims)
        claim_ids = next(find_first_single_claim)
        claim_id: ClaimID = claim_ids.pop()
        return str(claim_id.value)


class CounterMultipleClaims(Solver):

    def __call__(self):
        return len(list(filter(lambda x: len(x) > 1, self.fabric.space_claims)))
