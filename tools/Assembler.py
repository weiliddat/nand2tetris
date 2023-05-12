import os
import re
import sys
from typing import Literal


def read_file_lines(filepath: str) -> list[str]:
    code_matcher = re.compile("^\\s*(?!/)(\\S+)", re.MULTILINE)
    with open(filepath, "r") as f:
        return code_matcher.findall(f.read())


A_INSTRUCTION = Literal["A"]
C_INSTRUCTION = Literal["C"]
L_INSTRUCTION = Literal["L"]
INSTRUCTION_TYPE = Literal[A_INSTRUCTION, C_INSTRUCTION, L_INSTRUCTION]


# fmt: off
comp_codes = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "M":   "1110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "!M":  "1110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "-M":  "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101",
}
dest_codes = {
    None:  "000",
    "M":   "001",
    "D":   "010",
    "DM":  "011",
    "A":   "100",
    "AM":  "101",
    "AD":  "110",
    "ADM": "111",
}
jump_codes = {
    None:  "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}
# fmt: on


def instruction_type(line: str) -> INSTRUCTION_TYPE:
    if line.startswith("@"):
        return "A"
    if line.startswith("("):
        return "L"
    else:
        return "C"


def symb(line: str) -> str:
    symbol_matcher = re.compile("^[@(]+(\\S+?)[)]*$")
    symbol = symbol_matcher.match(line)
    if symbol is None:
        raise ValueError(f"No symbol found for {line}")
    return symbol and symbol.group(1)


def bin_symb(line: str) -> str:
    i = int(line)
    b = f"{i:0>15b}"
    return b


def bin_comp(line: str) -> str:
    return comp_codes[line]


def bin_dest(line: str | None) -> str:
    return dest_codes[line]


def bin_jump(line: str | None) -> str:
    return jump_codes[line]


def main():
    filepath = sys.argv[1]
    lines = read_file_lines(filepath)
    for n, l in enumerate(lines):
        ln = n + 1
        type = instruction_type(l)
        debug(l, ln, type)
        # if type == "A":
        #     print(f"0{bin_symb(symb(l))}")
        # if type == "C":
        #     print(f"111{bin_comp(comp(l))}{bin_dest(dest(l))}{bin_jump(jump(l))}")
        pass


def debug(l, ln, type):
    if os.environ.get("VERBOSE"):
        print(f"{ln} {l} {type}")
        if type == "A" or type == "L":
            print(f"symb {symb(l)}")
        else:
            dest_match = dest(l)
            if dest_match:
                print(f"dest {dest_match} {bin_dest(dest_match)}")
            comp_match = comp(l)
            if comp_match:
                print(f"comp {comp_match} {bin_comp(comp_match)}")
            jump_match = jump(l)
            if jump_match:
                print(f"jump {jump_match} {bin_jump(jump_match)}")


if __name__ == "__main__":
    main()
