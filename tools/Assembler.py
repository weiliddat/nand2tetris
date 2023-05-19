import os
import re
import sys
from typing import Literal, TypedDict


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
    "A":   "100",
    "DM":  "011",
    "MD":  "011",
    "AM":  "101",
    "MA":  "101",
    "AD":  "110",
    "DA":  "110",
    "ADM": "111",
    "AMD": "111",
    "MDA": "111",
    "MAD": "111",
    "DAM": "111",
    "DMA": "111",
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


def bin_symb(line: str | int) -> str:
    i = int(line)
    b = f"{i:0>15b}"
    return b


def bin_comp(line: str) -> str:
    return comp_codes[line]


def bin_dest(line: str | None) -> str:
    return dest_codes[line]


def bin_jump(line: str | None) -> str:
    return jump_codes[line]


class CInstructionParts(TypedDict):
    dest: str | None
    comp: str
    jump: str | None


def parse_c_instruction(line: str) -> CInstructionParts:
    matcher = re.compile(
        "^(?P<dest>[0ADM]+(?==))?=?(?P<comp>[!\\-+|&ADM01]+);?(?P<jump>(?<=;)[JMPGTEQLN]+)?$"
    )
    matches = matcher.match(line)
    if matches is None:
        raise ValueError(f"No dest/comp/jump found for {line}")
    else:
        return {
            "dest": matches.group("dest"),
            "comp": matches.group("comp"),
            "jump": matches.group("jump"),
        }


def main():
    asmpath = sys.argv[1]
    hackpath = get_hack_filepath(asmpath)
    lines = read_file_lines(asmpath)

    symbols = {
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576,
    }
    variable_ptr = 16

    ln = 0
    for l in lines:
        type = instruction_type(l)
        if type == "L":
            symbols[symb(l)] = ln
        else:
            ln += 1

    with open(hackpath, "w") as w:
        for l in lines:
            type = instruction_type(l)

            if type == "A":
                if symb(l) not in symbols:
                    if symb(l).isdigit():
                        symbols[symb(l)] = int(symb(l))
                    else:
                        symbols[symb(l)] = variable_ptr
                        variable_ptr += 1
                w.write(f"0{bin_symb(symbols[symb(l)])}\n")

            if type == "C":
                parts = parse_c_instruction(l)
                w.write(
                    f"111{bin_comp(parts['comp'])}{bin_dest(parts['dest'])}{bin_jump(parts['jump'])}\n"
                )


def get_hack_filepath(filepath):
    dirpath = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    filename_no_ext = os.path.splitext(filename)[0]
    outpath = os.path.join(dirpath, f"{filename_no_ext}.hack")
    return outpath


if __name__ == "__main__":
    main()
