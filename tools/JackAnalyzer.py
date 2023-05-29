import re
import sys
from parsimonious.grammar import Grammar

from utils import get_filepath_with_ext

jack_grammar = Grammar(
    r"""
    expr = (class / emptyline)*

    class = "class" ws class_name ws "{" ws class_var_dec* subroutine_dec* ws "}"
    class_var_dec = ("static" / "field") ws type ws var_name ("," ws? var_name)* semi ws
    type = "int" / "char" / "boolean" / class_name
    subroutine_dec = ("constructor" / "function" / "method") ws ("void" / type) ws subroutine_name ws? "(" parameter_list ")" ws? subroutine_body ws
    parameter_list = ((type ws var_name) ("," ws? type ws var_name))?
    subroutine_body = "{" ws var_dec* statements ws "}"
    var_dec = "var" ws type ws var_name ("," ws? var_name)* semi ws
    class_name = identifier
    subroutine_name = identifier
    var_name = identifier

    statements = statement*
    statement = let_statement / if_statement / while_statement / do_statement / return_statement
    let_statement = "let" ws var_name ("[" ws? expression ws? "]")? ws? "=" ws? expression semi ws
    if_statement = "if" ws? group_expression ws
        bracket_statements ws
        ("else" ws bracket_statements ws)?
    while_statement = "while" ws? group_expression ws bracket_statements ws
    do_statement = "do" ws subroutine_call semi ws
    return_statement = "return" ws expression? semi ws

    expression = term (ws? op ws? term)*
    term = integer_constant / string_constant / keyword_constant / subroutine_call / var_array / var_name / group_expression / unary_term
    unary_term = unary_op ws? term
    subroutine_call = subroutine_call_class_var / subroutine_call_this
    subroutine_call_this = subroutine_name "(" expression_list? ")"
    subroutine_call_class_var = identifier "." subroutine_name "(" expression_list? ")"
    expression_list = expression ws? ("," ws? expression)*
    op = "+" / "-" / "*" / "/" / "&" / "|" / "<" / ">" / "="
    unary_op = "-" / "~"
    keyword_constant = "true" / "false" / "null" / "this"

    var_array = var_name "[" ws? expression ws? "]"
    group_expression = "(" ws? expression ws? ")"
    bracket_statements = "{" ws? statements ws? "}"

    keyword = "class" / "constructor" / "function" / "method" / "field" / "static" /
        "var" / "int" / "char" / "boolean" / "void" / "true" / "false" / "null" / "this" /
        "let" / "do" / "if" / "else" / "while" / "return"
    symbol = "{" / "}" / "(" / ")" / "[" / "]" / "." / "," / ";" / "+" / "-" / "*" / "/" / "&" / "|" / "<" / ">" / "=" / "~"
    integer_constant = ~"[0-9]+"
    string_constant = "\"" ~"[^\"]*" "\""
    identifier = ~"[a-z]{1}[a-z0-9_]*"i

    ws = ~"\s*"
    emptyline = ws+
    semi = ws? ";"
    """
)


def strip_comments(input: str):
    # first group is for ignoring comments in strings
    comment_matcher = re.compile(
        r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE | re.DOTALL
    )

    def replacer(match):
        if match.group(2) is not None:
            return ""
        else:
            return match.group(1)

    results = comment_matcher.sub(replacer, input)

    return results


def main():
    jackpath = sys.argv[1]
    xmlpath = get_filepath_with_ext(jackpath, "xml")
    with open(jackpath, "r") as r:
        contents = r.read()
        stripped = strip_comments(contents)

        # print(jack_grammar)
        parsed = jack_grammar.parse(stripped)
        print(parsed)


if __name__ == "__main__":
    main()
