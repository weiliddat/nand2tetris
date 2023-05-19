from enum import Enum
import re
import sys
from textwrap import dedent
from typing import Literal


def read_file_lines(filepath: str) -> list[str]:
    code_matcher = re.compile("^\\s*(?!/)(.+)$", re.MULTILINE)
    with open(filepath, "r") as f:
        return code_matcher.findall(f.read())


class CommandType(Enum):
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_GOTO = 4
    C_IF = 5
    C_FUNCTION = 6
    C_RETURN = 7
    C_CALL = 8


def get_command_type(line: str) -> CommandType:
    if line.startswith("push"):
        return CommandType.C_PUSH
    elif line.startswith("pop"):
        return CommandType.C_POP
    elif line.startswith("label"):
        return CommandType.C_LABEL
    elif line.startswith("goto"):
        return CommandType.C_GOTO
    elif line.startswith("if-goto"):
        return CommandType.C_IF
    elif line.startswith("function"):
        return CommandType.C_FUNCTION
    elif line.startswith("return"):
        return CommandType.C_RETURN
    elif line.startswith("call"):
        return CommandType.C_CALL
    else:
        return CommandType.C_ARITHMETIC


def get_arg1(line: str) -> str:
    if get_command_type(line) == CommandType.C_ARITHMETIC:
        return line
    else:
        return line.split(" ")[1]


def get_arg2(line: str) -> int:
    return int(line.split(" ")[2])


def write_arithmetic(command: str):
    if command == "add":
        return dedent(
            """\
            @SP
            M=M-1
            A=M
            D=M
            A=A-1
            M=D+M"""
        )


def write_push_pop(
    command: Literal[CommandType.C_PUSH, CommandType.C_POP],
    segment: str,
    index: int,
):
    if command == CommandType.C_PUSH:
        if segment == "constant":
            return dedent(
                f"""\
                @{index}
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1"""
            )


def main():
    lines = read_file_lines(sys.argv[1])
    for line in lines:
        type = get_command_type(line)
        print(f"// {line}")
        if type == CommandType.C_ARITHMETIC:
            print(write_arithmetic(line))
        elif type == CommandType.C_PUSH or type == CommandType.C_POP:
            print(write_push_pop(type, get_arg1(line), get_arg2(line)))


if __name__ == "__main__":
    main()
