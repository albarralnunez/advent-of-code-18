from typing import IO

from src.day1.line_parser import LineParser
from src.day1.models import InstructionSet


class InputParser:

    def __init__(self, input_file: IO, line_parser: type(LineParser)):
        self._input_file = input_file
        self._line_parser = line_parser

    def parse(self):
        instructions = InstructionSet()
        for line in self._input_file.readlines():
            parser = self._line_parser(line)
            instruction = parser.parse()
            instructions.append(instruction)
        return instructions
