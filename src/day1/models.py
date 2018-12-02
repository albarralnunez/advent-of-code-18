import dataclasses
from enum import Enum


class InstructionType(Enum):

    increment = '+'
    decrement = '-'


@dataclasses.dataclass(frozen=True)
class Instruction:

    value: int
    instruction_type: InstructionType


@dataclasses.dataclass()
class InstructionSet(list):
    pass
