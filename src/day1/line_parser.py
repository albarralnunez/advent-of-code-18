from src.day1.exceptions import ParsingError
from src.day1.models import InstructionType, Instruction


class LineParser:

    INSTRUCTION_TYPE_ERROR_MESSAGE = "Lines must start with + or -."
    VALUE_ERROR_MESSAGE = "Value after operand must by a integer."

    def __init__(self, line: str):
        self._line = line

    def _parse_value(self):
        try:
            return int(self._line[1:])
        except ValueError:
            raise ParsingError()

    def _parse_instruction_type(self):
        if self._line.startswith("+"):
            return InstructionType.increment
        elif self._line.startswith("-"):
            return InstructionType.decrement
        else:
            raise ParsingError(self.INSTRUCTION_TYPE_ERROR_MESSAGE)

    def parse(self):
        instruction_type = self._parse_instruction_type()
        value = self._parse_value()
        return Instruction(value, instruction_type)
