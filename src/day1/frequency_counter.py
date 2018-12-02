import dataclasses
import operator
from typing import List

from src.day1.exceptions import NoResultError
from src.day1.models import InstructionType, Instruction


@dataclasses.dataclass
class FrequencyCounterBase:

    INSTRUCTIONS = {
        InstructionType.increment: operator.add,
        InstructionType.decrement: operator.sub
    }

    counter: int = 0

    def apply(self, *instructions: List[Instruction]):
        raise NotImplementedError


class FrequencyCounter(FrequencyCounterBase):
    def apply(self, *instructions: List[Instruction]):
        for instruction in instructions:
            op = self.INSTRUCTIONS[instruction.instruction_type]
            self.counter = op(self.counter, instruction.value)
        return self.counter


class FirstFrequencyMatch(FrequencyCounterBase):

    def apply(self, *instructions: List[Instruction]):
        values = {0}
        for instruction in instructions:
            op = self.INSTRUCTIONS[instruction.instruction_type]
            self.counter = op(self.counter, instruction.value)
            if self.counter in values:
                return self.counter
            values.add(self.counter)
        raise NoResultError(f"No result exception counter value {self.counter}.")
