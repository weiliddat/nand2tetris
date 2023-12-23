import re
import sys
from collections.abc import Sequence
from typing import Any

from parsimonious import NodeVisitor
from parsimonious.grammar import Grammar
from parsimonious.nodes import Node
from utils import flatten, get_filepath_with_ext

jack_grammar = Grammar(
    r"""
    expr = (class / emptyline)*

    class = keyword_class ws class_name ws symbol_open_curly ws
        class_var_dec* subroutine_dec* ws symbol_closed_curly
    class_var_dec = keyword_class_var ws type ws var_name (symbol_comma ws? var_name)* semi ws
    type = keyword_int / keyword_char / keyword_boolean / class_name
    subroutine_dec = keyword_class_subroutine ws (keyword_void / type) ws subroutine_name ws?
        symbol_open_round parameter_list symbol_closed_round ws? subroutine_body ws
    parameter_list = ((type ws var_name) (symbol_comma ws? type ws var_name)*)?
    subroutine_body = symbol_open_curly ws var_dec* statements ws symbol_closed_curly
    var_dec = keyword_var ws type ws var_name (symbol_comma ws? var_name)* semi ws
    class_name = identifier
    subroutine_name = identifier
    var_name = identifier

    statements = statement*
    statement = let_statement / if_statement / while_statement / do_statement / return_statement
    let_statement = keyword_let ws var_name (symbol_open_square ws? expression ws? symbol_closed_square)? ws?
        symbol_eq ws? expression semi ws
    if_statement = keyword_if ws? group_expression ws
        bracket_statements ws
        (keyword_else ws bracket_statements ws)?
    while_statement = keyword_while ws? group_expression ws bracket_statements ws
    do_statement = keyword_do ws subroutine_call semi ws
    return_statement = keyword_return ws expression? semi ws

    expression = term (ws? op ws? term)*
    term = integer_constant / string_constant / keyword_constant / subroutine_call /
        var_array / var_name / group_expression / unary_term
    unary_term = unary_op ws? term
    subroutine_call = subroutine_call_class_var / subroutine_call_this
    subroutine_call_this = subroutine_name symbol_open_round expression_list symbol_closed_round
    subroutine_call_class_var = identifier symbol_dot subroutine_name symbol_open_round expression_list symbol_closed_round
    expression_list = (expression ws? (symbol_comma ws? expression)*)?
    op = symbol_plus / symbol_minus / symbol_asterisk / symbol_slash /
        symbol_ampersand / symbol_pipe / symbol_lt / symbol_gt / symbol_eq
    unary_op = symbol_minus / symbol_tilde

    var_array = var_name symbol_open_square ws? expression ws? symbol_closed_square
    group_expression = symbol_open_round ws? expression ws? symbol_closed_round
    bracket_statements = symbol_open_curly ws? statements ws? symbol_closed_curly

    integer_constant = ~"[0-9]+"
    string_constant = "\"" ~"[^\"]*" "\""
    identifier = ~"[a-z]{1}[a-z0-9_]*"i

    keyword_class = "class"
    keyword_class_var = "static" / "field"
    keyword_class_subroutine = "constructor" / "function" / "method"
    keyword_constant = "true" / "false" / "null" / "this"
    keyword_var = "var"
    keyword_int = "int"
    keyword_char = "char"
    keyword_boolean = "boolean"
    keyword_void = "void"
    keyword_let = "let"
    keyword_if = "if"
    keyword_else = "else"
    keyword_while = "while"
    keyword_do = "do"
    keyword_return = "return"

    symbol_open_curly = "{"
    symbol_closed_curly = "}"
    symbol_open_round = "("
    symbol_closed_round = ")"
    symbol_open_square = "["
    symbol_closed_square = "]"
    symbol_dot = "."
    symbol_comma = ","
    symbol_semicolon = ";"
    symbol_plus = "+"
    symbol_minus = "-"
    symbol_asterisk = "*"
    symbol_slash = "/"
    symbol_ampersand = "&"
    symbol_pipe = "|"
    symbol_lt = "<"
    symbol_gt = ">"
    symbol_eq = "="
    symbol_tilde = "~"

    ws = ~"\\s*"
    emptyline = ws+
    semi = ws? symbol_semicolon
    """
)


class JackVisitorXml(NodeVisitor):
    def generic_visit(self, node: Node, visited_children: Sequence[Any]):
        return visited_children

    def visit_expr(self, node, visited_children):
        output = []
        output += flatten(visited_children)
        return output

    def visit_class(self, node, visited_children):
        return ["<class>", visited_children, "</class>"]

    def visit_string_constant(self, node, visited_children):
        return f"<stringConstant> {node.text[1:-1]} </stringConstant>"

    def visit_integer_constant(self, node, visited_children):
        return f"<integerConstant> {node.text} </integerConstant>"

    def visit_identifier(self, node, visited_children):
        return f"<identifier> {node.text} </identifier>"

    def visit_class_var_dec(self, node, visited_children):
        return ["<classVarDec>", visited_children, "</classVarDec>"]

    def visit_subroutine_dec(self, node, visited_children):
        return ["<subroutineDec>", visited_children, "</subroutineDec>"]

    def visit_parameter_list(self, node, visited_children):
        return ["<parameterList>", visited_children, "</parameterList>"]

    def visit_subroutine_body(self, node, visited_children):
        return ["<subroutineBody>", visited_children, "</subroutineBody>"]

    def visit_var_dec(self, node, visited_children):
        return ["<varDec>", visited_children, "</varDec>"]

    def visit_statements(self, node, visited_children):
        return ["<statements>", visited_children, "</statements>"]

    def visit_let_statement(self, node, visited_children):
        return ["<letStatement>", visited_children, "</letStatement>"]

    def visit_if_statement(self, node, visited_children):
        return ["<ifStatement>", visited_children, "</ifStatement>"]

    def visit_while_statement(self, node, visited_children):
        return ["<whileStatement>", visited_children, "</whileStatement>"]

    def visit_do_statement(self, node, visited_children):
        return ["<doStatement>", visited_children, "</doStatement>"]

    def visit_return_statement(self, node, visited_children):
        return ["<returnStatement>", visited_children, "</returnStatement>"]

    def visit_expression(self, node, visited_children):
        return ["<expression>", visited_children, "</expression>"]

    def visit_expression_list(self, node, visited_children):
        return ["<expressionList>", visited_children, "</expressionList>"]

    def visit_term(self, node, visited_children):
        return ["<term>", visited_children, "</term>"]

    # keywords

    def visit_keyword_class(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_class_var(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_class_subroutine(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_constant(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_var(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_int(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_char(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_boolean(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_void(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_let(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_if(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_else(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_while(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_do(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    def visit_keyword_return(self, n, v):
        return f"<keyword> {n.text} </keyword>"

    # symbols

    def visit_symbol_open_curly(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_closed_curly(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_open_round(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_closed_round(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_open_square(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_closed_square(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_dot(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_comma(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_semicolon(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_plus(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_minus(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_asterisk(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_slash(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_ampersand(self, n, v):
        return f"<symbol> &amp; </symbol>"

    def visit_symbol_pipe(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_lt(self, n, v):
        return f"<symbol> &lt; </symbol>"

    def visit_symbol_gt(self, n, v):
        return f"<symbol> &gt; </symbol>"

    def visit_symbol_eq(self, n, v):
        return f"<symbol> {n.text} </symbol>"

    def visit_symbol_tilde(self, n, v):
        return f"<symbol> {n.text} </symbol>"


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
        with open(xmlpath, "w") as w:
            contents = r.read()
            stripped = strip_comments(contents)

            tree = jack_grammar.parse(stripped)
            visitor = JackVisitorXml()
            output = visitor.visit(tree)
            w.writelines([l + "\n" for l in output])


if __name__ == "__main__":
    main()
