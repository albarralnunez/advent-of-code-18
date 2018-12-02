import pytest

from src.day1.frequency_counter import FirstFrequencyMatch
from src.day1.models import Instruction, InstructionType


@pytest.mark.parametrize("test_input,expected", [
    ([
        Instruction(value=2, instruction_type=InstructionType.increment),
        Instruction(value=1, instruction_type=InstructionType.increment),
        Instruction(value=3, instruction_type=InstructionType.decrement),
        Instruction(value=3, instruction_type=InstructionType.decrement),
    ], 0),
    ([
        Instruction(value=10, instruction_type=InstructionType.increment),
        Instruction(value=1, instruction_type=InstructionType.increment),
        Instruction(value=1, instruction_type=InstructionType.decrement),
    ], 10),
])
def test_first_frequency_march(test_input, expected):
    counter = FirstFrequencyMatch()
    result = counter.apply(*test_input)
    assert result == expected
