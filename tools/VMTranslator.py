import re
import sys
from enum import Enum
from textwrap import dedent
from typing import Literal

from utils import get_filename_no_ext, get_filepath_with_ext


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


jmpindex = 0


def write_arithmetic(command: str):
    global jmpindex
    jmpindex += 1

    if command == "add":
        return dedent(
            """\
            @SP
            M=M-1
            A=M
            D=M
            A=A-1
            M=M+D
            """
        )
    elif command == "sub":
        return dedent(
            """\
            @SP
            M=M-1
            A=M
            D=M
            A=A-1
            M=M-D
            """
        )
    elif command == "neg":
        return dedent(
            """\
            @SP
            A=M-1
            M=-M
            """
        )
    elif command == "eq":
        return dedent(
            f"""\
            @RET{jmpindex}
            D=A
            @RET
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @SP
            M=M-1
            A=M
            D=M-D
            @TRUE
            D;JEQ
            @FALSE
            0;JMP
            (RET{jmpindex})
            @SP
            M=M+1
            """
        )
    elif command == "lt":
        return dedent(
            f"""\
            @RET{jmpindex}
            D=A
            @RET
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @SP
            M=M-1
            A=M
            D=M-D
            @TRUE
            D;JLT
            @FALSE
            0;JMP
            (RET{jmpindex})
            @SP
            M=M+1
            """
        )
    elif command == "gt":
        return dedent(
            f"""\
            @RET{jmpindex}
            D=A
            @RET
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @SP
            M=M-1
            A=M
            D=M-D
            @TRUE
            D;JGT
            @FALSE
            0;JMP
            (RET{jmpindex})
            @SP
            M=M+1
            """
        )
    elif command == "and":
        return dedent(
            """\
            @SP
            M=M-1
            A=M
            D=M
            A=A-1
            M=M&D
            """
        )
    elif command == "or":
        return dedent(
            """\
            @SP
            M=M-1
            A=M
            D=M
            A=A-1
            M=M|D
            """
        )
    elif command == "not":
        return dedent(
            """\
            @SP
            A=M-1
            M=!M
            """
        )
    raise ValueError(f"Unknown arithmetic command {command}")


location_names = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT",
}


def write_push_pop(
    command: Literal[CommandType.C_PUSH, CommandType.C_POP],
    segment: str,
    index: int,
):
    address = ""

    if command == CommandType.C_PUSH:
        match (segment, index):
            case ("constant", index):
                address = dedent(
                    f"""\
                    @{index}
                    D=A
                    """
                )
            case ("local", index) | ("argument", index) | ("this", index) | (
                "that",
                index,
            ):
                location = location_names[segment]
                address = dedent(
                    f"""\
                    @{index}
                    D=A
                    @{location}
                    A=M+D
                    D=M
                    """
                )
            case ("pointer", 0):
                address = dedent(
                    f"""\
                    @THIS
                    D=M
                    """
                )
            case ("pointer", 1):
                address = dedent(
                    f"""\
                    @THAT
                    D=M
                    """
                )
            case ("temp", index):
                location = 5 + index
                address = dedent(
                    f"""\
                    @{location}
                    D=M
                    """
                )
            case ("static", index):
                address = dedent(
                    f"""\
                    @S{index}
                    D=M
                    """
                )

        return address + dedent(
            f"""\
            @SP
            A=M
            M=D
            @SP
            M=M+1
            """
        )
    elif command == CommandType.C_POP:
        match (segment, index):
            case ("local", index) | ("argument", index) | ("this", index) | (
                "that",
                index,
            ):
                location = location_names[segment]
                address = dedent(
                    f"""\
                    @{index}
                    D=A
                    @{location}
                    D=M+D
                    """
                )
            case ("pointer", 0):
                address = dedent(
                    f"""\
                    @THIS
                    D=A
                    """
                )
            case ("pointer", 1):
                address = dedent(
                    f"""\
                    @THAT
                    D=A
                    """
                )
            case ("temp", index):
                location = 5 + index
                address = dedent(
                    f"""\
                    @{location}
                    D=A
                    """
                )
            case ("static", index):
                address = dedent(
                    f"""\
                    @S{index}
                    D=A
                    """
                )

        return address + dedent(
            f"""\
            @R13
            M=D
            @SP
            M=M-1
            A=M
            D=M
            @R13
            A=M
            M=D
            """
        )
    raise ValueError(f"unknown command {command} {segment} {index}")


def write_label(label: str):
    return f"({label})"


def write_goto(label: str):
    return dedent(
        f"""\
        @{label}
        0;JMP
        """
    )


def write_if_goto(label: str):
    return dedent(
        f"""\
        @SP
        M=M-1
        A=M
        D=M
        @{label}
        D;JNE
        """
    )


def write_function(name: str, number_vars: int):
    code = f"@{name}\n"
    for _ in range(number_vars):
        code += write_push_pop(CommandType.C_PUSH, "constant", 0)
    return code


def write_return():
    return dedent(
        """\
        @LCL // frame = LCL
        D=M
        @R13
        M=D
        @5 // retAddr = *(frame-5)
        A=D-A
        D=M
        @R14
        M=D
        @SP // *ARG = pop()
        M=M-1
        A=M
        D=M
        @ARG
        A=M
        M=D
        @ARG // SP = ARG+1
        D=M+1
        @SP
        M=D
        @R13 // THAT = *(frame-1)
        AM=M-1
        D=M
        @THAT
        M=D
        @R13 // THIS = *(frame-2)
        AM=M-1
        D=M
        @THIS
        M=D
        @R13 // ARG = *(frame-3)
        AM=M-1
        D=M
        @ARG
        M=D
        @R13 // LCL = *(frame-4)
        AM=M-1
        D=M
        @LCL
        M=D
        @R14 // goto retAddr
        A=M
        0;JMP
        """
    )


def write_end_loop():
    return dedent(
        """\
        @END_LOOP
        0;JMP
        (TRUE)
        @SP
        A=M
        M=-1
        @RET
        A=M
        0;JMP
        (FALSE)
        @SP
        A=M
        M=0
        @RET
        A=M
        0;JMP
        (END_LOOP)
        @END_LOOP
        0;JMP
        """
    )


def main():
    asmpath = sys.argv[1]
    hackpath = get_filepath_with_ext(asmpath, "asm")
    filename = get_filename_no_ext(asmpath)
    lines = read_file_lines(asmpath)

    with open(hackpath, "w") as w:
        function_prefix = f"{filename}."
        return_index = 0
        for line in lines:
            type = get_command_type(line)
            w.write(f"// {line}\n")
            if type == CommandType.C_ARITHMETIC:
                w.write(write_arithmetic(line))
            elif type == CommandType.C_PUSH or type == CommandType.C_POP:
                w.write(write_push_pop(type, get_arg1(line), get_arg2(line)))
            elif type == CommandType.C_LABEL:
                w.write(write_label(function_prefix + get_arg1(line)))
            elif type == CommandType.C_GOTO:
                w.write(write_goto(function_prefix + get_arg1(line)))
            elif type == CommandType.C_IF:
                w.write(write_if_goto(function_prefix + get_arg1(line)))
            elif type == CommandType.C_FUNCTION:
                function_name = get_arg1(line)
                number_vars = get_arg2(line)
                function_prefix += f"{function_name}$"
                w.write(write_function(f"{filename}.{function_name}", number_vars))
            elif type == CommandType.C_CALL:
                pass
            elif type == CommandType.C_RETURN:
                w.write(write_return())
        w.write(write_end_loop())


if __name__ == "__main__":
    main()
