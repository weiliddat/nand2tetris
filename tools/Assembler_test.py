from Assembler import parse_c_instruction


class TestParseCInstruction:
    def test_parse_dest(self):
        input = "D=M"
        expected = "D"
        assert parse_c_instruction(input).get("dest") == expected

        input = "D=M"
        expected = "D"
        assert parse_c_instruction(input).get("dest") == expected

    def test_parse_comp(self):
        input = "D=M"
        expected = "M"
        assert parse_c_instruction(input).get("comp") == expected

        input = "D=M-1"
        expected = "M-1"
        assert parse_c_instruction(input).get("comp") == expected

    def test_parse_jump(self):
        input = "0;JMP"
        expected = "JMP"
        assert parse_c_instruction(input).get("jump") == expected

        input = "A=D;JGT"
        expected = "JGT"
        assert parse_c_instruction(input).get("jump") == expected

    def test_parse_all(self):
        input = "D=A;JGT"
        expected = {"dest": "D", "comp": "A", "jump": "JGT"}
        assert parse_c_instruction(input) == expected

        input = "D=M"
        expected = {"dest": "D", "comp": "M", "jump": None}
        assert parse_c_instruction(input) == expected

        input = "0;JMP"
        expected = {"dest": None, "comp": "0", "jump": "JMP"}
        assert parse_c_instruction(input) == expected

        input = "D=M-1"
        expected = {"dest": "D", "comp": "M-1", "jump": None}
        assert parse_c_instruction(input) == expected

        input = "D;JEQ"
        expected = {"dest": None, "comp": "D", "jump": "JEQ"}
        assert parse_c_instruction(input) == expected

        input = "D=D-M"
        expected = {"dest": "D", "comp": "D-M", "jump": None}
        assert parse_c_instruction(input) == expected

        input = "D=D-M;JGT"
        expected = {"dest": "D", "comp": "D-M", "jump": "JGT"}
        assert parse_c_instruction(input) == expected

        input = "M=D+A"
        expected = {"dest": "M", "comp": "D+A", "jump": None}
        assert parse_c_instruction(input) == expected
