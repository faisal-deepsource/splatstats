from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from toolz.dicttoolz import get_in, update_in, dissoc
from ...tools import get_size
import regex
from .models import (
    Battle,
    Weapons,
    MainAbilities,
    SubAbilities,
    Stage,
    Clothes,
    Headgear,
    Shoes,
    WeaponFamily,
    WeaponSubs,
    WeaponSpecials,
)

(
    ATTR,
    INTEGER,
    BOOL,
    STRING,
    FLOAT,
    GREATERTHAN,
    LESSTHAN,
    EQUAL,
    GREATEREQUAL,
    LESSEQUAL,
    PLUS,
    MINUS,
    MULTIPLY,
    DIVIDE,
    OR,
    AND,
    NOT,
    LPAREN,
    RPAREN,
    VAR,
    ASSIGN,
    NEWLINE,
    LBRACKET,
    RBRACKET,
    LSQUIGGLE,
    RSQUIGGLE,
    SIZEOF,
    IF,
    ELSE,
    FUNCT,
    WHILE,
    CALL, 
    EOL,
) = (
    "ATTR",
    "INTEGER",
    "BOOLEAN",
    "STRING",
    "FLOAT",
    ">",
    "<",
    "==",
    ">=",
    "<=",
    "+",
    "-",
    "*",
    "/",
    "OR",
    "AND",
    "NOT",
    "(",
    ")",
    "VAR",
    ":=",
    "\n",
    "[",
    "]",
    "{",
    "}",
    "SIZEOF",
    "IF",
    "ELSE",
    "FUNCT",
    "WHILE",
    "CALL",
    "",
)


class Token:
    def __init__(self, category, value):
        self.type = category
        self.value = value

    def __str__(self):
        """String representation of the class instance."""
        return "Token({type}, {value})".format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()


class Lexer:
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos[-1] is an index into self.text
        self.pos = [0]
        self.current_char = self.text[self.pos[-1]]

    def push_pos(self, pos_val):
        self.pos.append(pos_val)

    def pop_pos(self):
        return self.pos.pop()

    def get_pos(self):
        return self.pos[-1]

    @staticmethod
    def error():
        raise Exception("Invalid character")

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos[-1] += 1
        if self.pos[-1] > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos[-1]]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def num(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ""
        while self.current_char is not None and (
            self.current_char.isdigit() or self.current_char == "."
        ):
            result += self.current_char
            self.advance()
        try:
            return int(result)
        except:
            return float(result)

    def string(self):
        """Return a string consumed from the input."""
        result = ""
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()
        return result

    def attr_set(self):
        result = ""
        while self.current_char is not None and not self.current_char.isspace():
            result += self.current_char
            self.advance()
        if regex.search(
            "(rule)|(match_type)|(stage)|(win(_meter)?)|(has_disconnected_player)|(((my)|(other))_team_count)|((elapsed_)?time)|(tag_id)|(battle_number)|(((league)|(splatfest))_point)|(splatfest_title_after)|(player_x_power)|(((player)|(teammate_[a-c])|(opponent_[a-d]))_(((headgear)|(clothes)|(shoes))(_((sub[0-2])|(main)))?|(weapon)|(rank)|(level(_star)?)|(kills)|(deaths)|(assists)|(specials)|(game_paint_point)|(splatfest_title)|(name)|(splatnet_id)|(gender)|(species)))$",
            result,
        ):
            return Token(ATTR, result)
        return Token(VAR, result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char == "\r":
                self.advance()
                if self.current_char == "\n":
                    self.advance()
                    return Token(NEWLINE, "\n")

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == "[":
                self.advance()
                return Token(LBRACKET, "[")

            if self.current_char == "]":
                self.advance()
                return Token(RBRACKET, "]")

            if self.current_char == "T":
                self.advance()
                return Token(BOOL, True)

            if self.current_char == "F":
                self.advance()
                if self.current_char == "U":
                    self.advance()
                    if self.current_char == "N":
                        self.advance()
                        if self.current_char == "C":
                            self.advance()
                            if self.current_char == "T":
                                self.advance()
                                return Token(FUNCT, "FUNCT")
                    self.error()
                return Token(BOOL, False)

            if self.current_char == "A":
                self.advance()
                if self.current_char == "N":
                    self.advance()
                    if self.current_char == "D":
                        self.advance()
                        return Token(AND, "AND")
                self.error()

            if self.current_char == "N":
                self.advance()
                if self.current_char == "O":
                    self.advance()
                    if self.current_char == "T":
                        self.advance()
                        return Token(NOT, "NOT")
                self.error()

            if self.current_char == "O":
                self.advance()
                if self.current_char == "R":
                    self.advance()
                    return Token(OR, "OR")
                self.error()

            if self.current_char == "I":
                self.advance()
                if self.current_char == "F":
                    self.advance()
                    return Token(IF, "IF")
                self.error()

            if self.current_char == "E":
                self.advance()
                if self.current_char == "L":
                    self.advance()
                    if self.current_char == "S":
                        self.advance()
                        if self.current_char == "E":
                            self.advance()
                            return Token(ELSE, "ELSE")
                self.error()
            
            if self.current_char == "C":
                self.advance()
                if self.current_char == "A":
                    self.advance()
                    if self.current_char == "L":
                        self.advance()
                        if self.current_char == "L":
                            self.advance()
                            return Token(CALL, "CALL")
                self.error()

            if self.current_char == "S":
                self.advance()
                if self.current_char == "I":
                    self.advance()
                    if self.current_char == "Z":
                        self.advance()
                        if self.current_char == "E":
                            self.advance()
                            if self.current_char == "O":
                                self.advance()
                                if self.current_char == "F":
                                    self.advance()
                                    return Token(SIZEOF, "SIZEOF")
                self.error()

            if self.current_char == "W":
                self.advance()
                if self.current_char == "H":
                    self.advance()
                    if self.current_char == "I":
                        self.advance()
                        if self.current_char == "L":
                            self.advance()
                            if self.current_char == "E":
                                self.advance()
                                return Token(WHILE, "WHILE")
                self.error()

            if self.current_char.isalpha():
                return self.attr_set()

            if self.current_char == '"':
                self.advance()
                return Token(STRING, self.string())

            if self.current_char.isdigit():
                num = self.num()
                if type(num) is float:
                    return Token(FLOAT, num)
                return Token(INTEGER, num)

            if self.current_char == "=":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(EQUAL, "==")
                self.error()

            if self.current_char == ":":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(ASSIGN, ":=")
                self.error()

            if self.current_char == ">":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(GREATEREQUAL, ">=")
                return Token(GREATERTHAN, ">")

            if self.current_char == "<":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(LESSEQUAL, "<=")
                return Token(LESSTHAN, "<")

            if self.current_char == "(":
                self.advance()
                return Token(LPAREN, "(")

            if self.current_char == ")":
                self.advance()
                return Token(RPAREN, ")")

            if self.current_char == "{":
                self.advance()
                return Token(LSQUIGGLE, "{")

            if self.current_char == "}":
                self.advance()
                return Token(RSQUIGGLE, "}")

            if self.current_char == "+":
                self.advance()
                return Token(PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(MINUS, "-")

            if self.current_char == "*":
                self.advance()
                return Token(MULTIPLY, "*")

            if self.current_char == "/":
                self.advance()
                return Token(DIVIDE, "/")

            self.error()

        return Token(EOL, None)


def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


class Interpreter:
    """
    line : (VAR ASSIGN term NEWLINE) | (term (NEWLINE)?) | (FUNCT VAR LBRACKET (line)+ RBRACKET NEWLINE)
    term : (expr) | (LPAREN term (OR | AND) term RPAREN) | (NOT LPAREN term RPAREN) | (IF expr LBRACKET NEWLINE (line)* NEWLINE RBRACKET ELSE LBRACKET NEWLINE (line)+ RBRACKET)
    expr : (VAR) | (SIZEOF VAR (GREATERTHAN | GREATEREQUAL | LESSTHAN | LESSEQUAL | EQUAL) INTEGER) | (ATTR (GREATERTHAN | GREATEREQUAL | LESSTHAN | LESSEQUAL | EQUAL) value)
    value: INTEGER | FLOAT | STRING | BOOL
    """

    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()
        self.vars = [{}]
        self.switch_comp = {
            GREATERTHAN: lambda a, b: a > b,
            LESSTHAN: lambda a, b: a < b,
            GREATEREQUAL: lambda a, b: a >= b,
            LESSEQUAL: lambda a, b: a <= b,
            EQUAL: lambda a, b: a == b,
        }
        self.switch_query = {
            GREATERTHAN: "__gt",
            LESSTHAN: "__lt",
            GREATEREQUAL: "__gte",
            LESSEQUAL: "__lte",
            EQUAL: "",
        }
        self.switch_math = {
            PLUS: lambda a, b: a + b,
            MINUS: lambda a, b: a - b,
            MULTIPLY: lambda a, b: a * b,
            DIVIDE: lambda a, b: a / b,
        }

    @staticmethod
    def error():
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        # print(self.current_token.type + " " + token_type)
        if self.current_token.type == token_type:
            if len(self.lexer.pos) > 0:
                self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def interpret(self):
        result = None
        while result is None:
            result = self.line()
        return result

    def line(self, evaluate=True):
        """line: (VAR ASSIGN term NEWLINE) | (term (NEWLINE)?) | (FUNCT VAR LPAREN (VAR)* RPAREN LSQUIGGLE NEWLINE (line)+ RSQUIGGLE NEWLINE) | (WHILE LPAREN expr RPAREN LSQUIGGLE NEWLINE (line)+ RSQUIGGLE NEWLINE)"""
        if self.current_token.type is VAR:
            return self.line_var_handler(evaluate)
        if self.current_token.type is WHILE:
            return self.while_handler(evaluate)
        if self.current_token.type is FUNCT:
            return self.funct_handler(evaluate)
        val = self.term(evaluate)
        if self.current_token.type is NEWLINE:
            self.eat(NEWLINE)
        return val

    def line_var_handler(self, evaluate=True):
        var_name = self.current_token.value
        self.eat(VAR)
        if self.current_token.type is ASSIGN:
            self.eat(ASSIGN)
            term = self.term(evaluate)
            self.set_var(var_name, term, evaluate)
            if self.current_token.type is NEWLINE:
                self.eat(NEWLINE)
            return None
        val = self.get_var(var_name)
        return val

    def set_var(self, var_name, var_value, evaluate=True):
        # print(str(var_name) + " " + str(var_value) + " " + str(evaluate))
        if evaluate:
            self.vars[-1][var_name] = var_value
            # print(get_size(self.vars))
            # print(len(self.vars))
            # print(self.vars)

    def funct_handler(self, evaluate=True):
        self.eat(FUNCT)
        funct_name = self.current_token.value
        self.eat(VAR)
        params = {}
        self.eat(LPAREN)
        while self.current_token.type is not RPAREN:
            params[self.current_token.value] = None
            self.eat(VAR)
        self.eat(RPAREN)
        self.eat(LSQUIGGLE)
        pos = self.lexer.get_pos()
        self.eat(NEWLINE)
        self.set_var(funct_name, {"pos": pos, "params": params}, evaluate)
        while self.current_token.type is not RSQUIGGLE:
            self.line(False)
        self.eat(RSQUIGGLE)
        self.eat(NEWLINE)

    def while_handler(self, evaluate=True):
        self.eat(WHILE)
        start_pos = self.lexer.get_pos()
        self.eat(LPAREN)
        while self.expr(evaluate):
            curr_pos = self.lexer.get_pos()
            self.eat(RPAREN)
            self.lexer.push_pos(start_pos)
            self.lexer.push_pos(curr_pos)
            self.current_token = self.lexer.get_next_token()
            self.eat(LSQUIGGLE)
            self.eat(NEWLINE)
            while self.current_token.type is not RSQUIGGLE:
                result = self.line(evaluate)
            self.lexer.pop_pos()
            self.lexer.advance()
            self.current_token = self.lexer.get_next_token()
        self.eat(RPAREN)
        self.eat(LSQUIGGLE)
        self.eat(NEWLINE)
        while self.current_token.type is not RSQUIGGLE:
            self.line(False)
        self.eat(RSQUIGGLE)
        self.eat(NEWLINE)
        return None

    def if_handler(self, evaluate=True):
        self.eat(IF)
        self.eat(LPAREN)
        if self.expr(evaluate):
            self.eat(RPAREN)
            self.eat(LSQUIGGLE)
            self.eat(NEWLINE)
            while self.current_token.type is not RSQUIGGLE:
                self.line(evaluate)
            self.eat(RSQUIGGLE)
            self.eat(ELSE)
            self.eat(LSQUIGGLE)
            self.eat(NEWLINE)
            while self.current_token.type is not RSQUIGGLE:
                self.line(False)
            self.eat(RSQUIGGLE)
            if self.current_token.type is NEWLINE:
                self.eat(NEWLINE)
            return None
        self.eat(RPAREN)
        self.eat(LSQUIGGLE)
        self.eat(NEWLINE)
        while self.current_token.type is not RSQUIGGLE:
            self.line(False)
        self.eat(RSQUIGGLE)
        self.eat(ELSE)
        self.eat(LSQUIGGLE)
        self.eat(NEWLINE)
        while self.current_token.type is not RSQUIGGLE:
            self.line(evaluate)
        self.eat(RSQUIGGLE)
        if self.current_token.type is NEWLINE:
            self.eat(NEWLINE)
        return None

    def not_handler(self, evaluate=True):
        self.eat(NOT)
        self.eat(LPAREN)
        to_exclude = self.term(evaluate)
        if evaluate:
            result = (
                Battle.objects.all().exclude(id__in=to_exclude).order_by("-time")
            )
        else:
            result = Battle.objects.none()
        self.eat(RPAREN)
        return result

    def term_lparen_handler(self, evaluate=True):
        self.eat(LPAREN)
        set_a = self.term(evaluate)
        token = self.current_token
        result = Battle.objects.none()
        if token.type == OR:
            self.eat(OR)
            set_b = self.term(evaluate)
            if evaluate:
                result = set_a | set_b
                result = result.order_by("-time")
            self.eat(RPAREN)
        elif token.type == AND:
            self.eat(AND)
            set_b = self.term(evaluate)
            if evaluate:
                result = set_a & set_b
                result = result.order_by("-time")
            self.eat(RPAREN)
        return result

    def term(self, evaluate=True):
        """term: (expr) | (LPAREN term (OR | AND) term RPAREN) | (NOT LPAREN term RPAREN) | (IF expr LSQUIGGLE NEWLINE (line)* NEWLINE RSQUIGGLE ELSE LSQUIGGLE NEWLINE (line)+ RSQUIGGLE)"""
        if self.current_token.type is IF:
            return self.if_handler(evaluate)
        if self.current_token.type is NOT:
            return self.not_handler(evaluate)
        if self.current_token.type is LPAREN:
            return self.term_lparen_handler(evaluate)
        return self.expr(evaluate)

    def value(self):
        """value: (INTEGER) | (FLOAT) | (STRING) | (BOOL)"""
        token = self.current_token
        switch = {
            BOOL: BOOL,
            INTEGER: INTEGER,
            FLOAT: FLOAT,
            STRING: STRING,
        }
        self.eat(switch.get(token.type))
        return token.value

    def comp_operator(self, token_type, a, b):
        """(GREATERTHAN) | (GREATEREQUAL) | (LESSTHAN) | (LESSEQUAL) | (EQUAL)"""
        return self.switch_comp[token_type](a=a, b=b)

    def query_operator(self, token_type):
        """(GREATERTHAN) | (GREATEREQUAL) | (LESSTHAN) | (LESSEQUAL) | (EQUAL)"""
        return self.switch_query[token_type]

    def math_operator(self, token_type, a, b):
        """(GREATERTHAN) | (GREATEREQUAL) | (LESSTHAN) | (LESSEQUAL) | (EQUAL)"""
        return self.switch_math[token_type](a=a, b=b)

    def get_var(self, var_name, layer=-1):
        #for i in range(-1, -len(self.vars)-1, -1):
        if var_name in self.vars[layer]:
            return self.vars[layer][var_name]
        return None

    def call_handler(self, evaluate=True):
        self.eat(CALL)
        func_name = self.current_token.value
        self.eat(VAR)
        self.eat(LPAREN)
        params = self.get_var(func_name, 0)["params"].copy()
        i = 0
        while self.current_token.type is not RPAREN:
            params[list(params)[i][0]] = self.term(evaluate)
            i += 1
        return_pos = self.lexer.get_pos()
        self.eat(RPAREN)
        result = None
        if evaluate:
            func_loc = self.get_var(func_name, 0)["pos"]
            self.lexer.pop_pos()
            self.lexer.push_pos(return_pos - 1)
            self.lexer.push_pos(func_loc - 1)
            self.vars.append(params)
            self.lexer.advance()
            self.current_token = self.lexer.get_next_token()
            while self.current_token.type is not RSQUIGGLE:
                result = self.line(evaluate)
            self.vars.pop()
            print("result count: " + str(result.count() if result is not None else None))
            self.lexer.pop_pos()
            self.eat(RSQUIGGLE)
        return result

    def expr(self, evaluate=True):
        """expr: (CALL VAR LPAREN (term)? RPAREN) | (VAR) | (value) | (SIZEOF LBRACKET term RBRACKET) | (ATTR query_operator term) | (term (comp_operator | math_operator) term)"""
        if self.current_token.type is CALL:
            return self.call_handler(evaluate)
        if self.current_token.type is SIZEOF:
            self.eat(SIZEOF)
            self.eat(LPAREN)
            set_a = self.term(evaluate)
            if isinstance(set_a, QuerySet):
                set_a_size = set_a.count()
            else:
                if type(set_a) is int:
                    set_a_size = set_a
                else:
                    set_a_size = 0
            self.eat(RPAREN)
            token = self.current_token
            if token.type in self.switch_comp:
                self.eat(token.type)
            else:
                return set_a_size
            if self.current_token.type == SIZEOF:
                self.eat(SIZEOF)
                self.eat(LPAREN)
                if self.current_token.type is VAR:
                    if evaluate:
                        set_b_size = self.get_var(self.current_token.value)
                        if isinstance(set_b_size, QuerySet):
                            set_b_size = set_b_size.count()
                        if type(set_b_size) is not int:
                            self.error()
                    else:
                        set_b_size = 0
                    self.eat(VAR)
                else:
                    set_b_size = self.term(evaluate)
                    if type(set_b_size) is QuerySet:
                        set_b_size = set_b_size.count()
                    if type(set_b_size) is not int:
                        self.error()
            else:
                set_b_size = self.value()
                if type(set_b_size) is not int:
                    self.error()
            self.eat(RPAREN)
            return self.comp_operator(token.type, set_a_size, set_b_size)
        if self.current_token.type is VAR:
            val_a = self.get_var(self.current_token.value)
            if val_a is None:
                val_a = 0
            self.eat(VAR)
            token = self.current_token
            if token.type in self.switch_comp:
                self.eat(token.type)
            else:
                if token.type in self.switch_math:
                    self.eat(token.type)
                    val_b = self.term(evaluate)
                    if evaluate and (
                        (type(val_a) is not int and type(val_a) is not float)
                        or (type(val_b) is not int and type(val_b) is not float)
                    ):
                        self.error()
                    return self.math_operator(token.type, val_a, val_b)
                return val_a
            val_b = self.term(evaluate)
            if evaluate:
                result_value = self.comp_operator(token.type, val_a, val_b)
            else:
                result_value = False
            return result_value
        if self.current_token.type in (BOOL, INTEGER, FLOAT, STRING):
            val_a = self.value()
            token = self.current_token.type
            if token in self.switch_comp:
                self.eat(token)
                val_b = self.term()
                return self.comp_operator(token, val_a, val_b)
            if token in self.switch_math:
                self.eat(token)
                val_b = self.term()
                if (type(val_a) is not int and type(val_a) is not float) or (
                    type(val_b) is not int and type(val_b) is not float
                ):
                    self.error()
                return self.math_operator(token.type, val_a, val_b)
            return val_a
        attribute = self.current_token.value
        self.eat(ATTR)
        if regex.search(
            "(rule)|(match_type)|(stage)|(win(_meter)?)|(has_disconnected_player)|(((my)|(other))_team_count)|((elapsed_)?time)|(tag_id)|(battle_number)|(((league)|(splatfest))_point)|(splatfest_title_after)|(player_x_power)|(((player)|(teammate_[a-c])|(opponent_[a-d]))_(((headgear)|(clothes)|(shoes))(_((sub[0-2])|(main)))?|(weapon)|(rank)|(level(_star)?)|(kills)|(deaths)|(assists)|(specials)|(game_paint_point)|(splatfest_title)|(name)|(splatnet_id)|(gender)|(species)))$",
            attribute,
        ):
            mapping = {
                "abcd-abc": {},
                "abcd-acb": {},
                "abcd-bac": {},
                "abcd-bca": {},
                "abcd-cab": {},
                "abcd-cba": {},
                "abdc-abc": {},
                "abdc-acb": {},
                "abdc-bac": {},
                "abdc-bca": {},
                "abdc-cab": {},
                "abdc-cba": {},
                "acbd-abc": {},
                "acbd-acb": {},
                "acbd-bac": {},
                "acbd-bca": {},
                "acbd-cab": {},
                "acbd-cba": {},
                "acdb-abc": {},
                "acdb-acb": {},
                "acdb-bac": {},
                "acdb-bca": {},
                "acdb-cab": {},
                "acdb-cba": {},
                "adbc-abc": {},
                "adbc-acb": {},
                "adbc-bac": {},
                "adbc-bca": {},
                "adbc-cab": {},
                "adbc-cba": {},
                "adcb-abc": {},
                "adcb-acb": {},
                "adcb-bac": {},
                "adcb-bca": {},
                "adcb-cab": {},
                "adcb-cba": {},
                "bacd-abc": {},
                "bacd-acb": {},
                "bacd-bac": {},
                "bacd-bca": {},
                "bacd-cab": {},
                "bacd-cba": {},
                "badc-abc": {},
                "badc-acb": {},
                "badc-bac": {},
                "badc-bca": {},
                "badc-cab": {},
                "badc-cba": {},
                "bcad-abc": {},
                "bcad-acb": {},
                "bcad-bac": {},
                "bcad-bca": {},
                "bcad-cab": {},
                "bcad-cba": {},
                "bcda-abc": {},
                "bcda-acb": {},
                "bcda-bac": {},
                "bcda-bca": {},
                "bcda-cab": {},
                "bcda-cba": {},
                "bdac-abc": {},
                "bdac-acb": {},
                "bdac-bac": {},
                "bdac-bca": {},
                "bdac-cab": {},
                "bdac-cba": {},
                "bdca-abc": {},
                "bdca-acb": {},
                "bdca-bac": {},
                "bdca-bca": {},
                "bdca-cab": {},
                "bdca-cba": {},
                "cabd-abc": {},
                "cabd-acb": {},
                "cabd-bac": {},
                "cabd-bca": {},
                "cabd-cab": {},
                "cabd-cba": {},
                "cadb-abc": {},
                "cadb-acb": {},
                "cadb-bac": {},
                "cadb-bca": {},
                "cadb-cab": {},
                "cadb-cba": {},
                "cbad-abc": {},
                "cbad-acb": {},
                "cbad-bac": {},
                "cbad-bca": {},
                "cbad-cab": {},
                "cbad-cba": {},
                "cbda-abc": {},
                "cbda-acb": {},
                "cbda-bac": {},
                "cbda-bca": {},
                "cbda-cab": {},
                "cbda-cba": {},
                "cdab-abc": {},
                "cdab-acb": {},
                "cdab-bac": {},
                "cdab-bca": {},
                "cdab-cab": {},
                "cdab-cba": {},
                "cdba-abc": {},
                "cdba-acb": {},
                "cdba-bac": {},
                "cdba-bca": {},
                "cdba-cab": {},
                "cdba-cba": {},
                "dabc-abc": {},
                "dabc-acb": {},
                "dabc-bac": {},
                "dabc-bca": {},
                "dabc-cab": {},
                "dabc-cba": {},
                "dacb-abc": {},
                "dacb-acb": {},
                "dacb-bac": {},
                "dacb-bca": {},
                "dacb-cab": {},
                "dacb-cba": {},
                "dbac-abc": {},
                "dbac-acb": {},
                "dbac-bac": {},
                "dbac-bca": {},
                "dbac-cab": {},
                "dbac-cba": {},
                "dbca-abc": {},
                "dbca-acb": {},
                "dbca-bac": {},
                "dbca-bca": {},
                "dbca-cab": {},
                "dbca-cba": {},
                "dcab-abc": {},
                "dcab-acb": {},
                "dcab-bac": {},
                "dcab-bca": {},
                "dcab-cab": {},
                "dcab-cba": {},
                "dcba-abc": {},
                "dcba-acb": {},
                "dcba-bac": {},
                "dcba-bca": {},
                "dcba-cab": {},
                "dcba-cba": {},
            }
            switch = {
                GREATERTHAN: "__gt",
                LESSTHAN: "__lt",
                GREATEREQUAL: "__gte",
                LESSEQUAL: "__lte",
                EQUAL: "",
            }
            token = self.current_token
            if token.type in switch:
                self.eat(token.type)
            else:
                self.error()
            value = self.term(evaluate)
            if regex.search(
                "((player)|(teammate_[a-c])|(opponent_[a-d]))_weapon",
                attribute,
            ):
                value_a = [x for (x, y) in Weapons if y == value]
                if len(value_a) > 0:
                    value = value_a[0]
            elif regex.search(
                "((player)|(teammate_[a-c])|(opponent_[a-c]))_((headgear)|(clothes)|(shoes))_main",
                attribute,
            ):
                value_a = [x for (x, y) in MainAbilities if y == value]
                if len(value_a) > 0:
                    value = value_a[0]
            elif regex.search(
                "((player)|(teammate_[a-c])|(opponent_[a-c]))_((headgear)|(clothes)|(shoes))_sub[0-2]",
                attribute,
            ):
                value_a = [x for (x, y) in SubAbilities if y == value]
                if len(value_a) > 0:
                    value = value_a[0]
            elif regex.search("stage", attribute):
                value_a = [x for (x, y) in Stage if y == value]
                if len(value_a) > 0:
                    value = value_a[0]
            elif regex.search(
                "((player)|(teammate_[a-c])|(opponent_[a-c]))_headgear", attribute
            ):
                value_a = [x for (x, y) in Headgear if y == value]
                if len(value_a) > 0:
                    value = value_a[0]
            elif regex.search(
                "((player)|(teammate_[a-c])|(opponent_[a-c]))_clothes", attribute
            ):
                value_a = [x for (x, y) in Clothes if y == value]
                if len(value_a) > 0:
                    value = value_a[0]
            elif regex.search(
                "((player)|(teammate_[a-c])|(opponent_[a-c]))_shoes", attribute
            ):
                value_a = [x for (x, y) in Shoes if y == value]
                if len(value_a) > 0:
                    value = value_a[0]
            if regex.search(
                "((teammate_[a-c])|(opponent_[a-d]))_[0-z_]*",
                attribute,
            ):
                for key in mapping.keys():
                    if attribute[0:8] == "teammate":
                        mapping[key][
                            "{}{}{}{}".format(
                                attribute[0:8],
                                find_2nd(key, attribute[9]) - 5,
                                attribute[10:],
                                self.query_operator(token.type),
                            )
                        ] = value
                    else:
                        mapping[key][
                            "{}{}{}{}".format(
                                attribute[0:8],
                                key.index(attribute[9]),
                                attribute[10:],
                                self.query_operator(token.type),
                            )
                        ] = value
            else:
                for key in mapping.keys():
                    mapping[key][
                        attribute + self.query_operator(token.type)
                    ] = value
            battles = Battle.objects.none()
            for key in mapping:
                battles = battles | Battle.objects.filter(**(mapping[key]))
            battles = battles.order_by("-time")
            return battles
        token = self.current_token
        self.eat(token.type)
        value = self.value()
        if regex.search(
            "((player)|(teammate_[a-c])|(oppponent_[a-d]))_weapon_family", attribute
        ):
            value_a = [x for (x, y) in WeaponFamily if y == value]
            if len(value_a) > 0:
                value = value_a[0]
        if regex.search(
            "((player)|(teammate_[a-c])|(oppponent_[a-d]))_weapon_sub", attribute
        ):
            value_a = [x for (x, y) in WeaponSubs if y == value]
            if len(value_a) > 0:
                value = value_a[0]
        if regex.search(
            "((player)|(teammate_[a-c])|(oppponent_[a-d]))_weapon_special",
            attribute,
        ):
            value_a = [x for (x, y) in WeaponSpecials if y == value]
            if len(value_a) > 0:
                value = value_a[0]
        mapping = {
            "abcd-abc": [],
            "abcd-acb": [],
            "abcd-bac": [],
            "abcd-bca": [],
            "abcd-cab": [],
            "abcd-cba": [],
            "abdc-abc": [],
            "abdc-acb": [],
            "abdc-bac": [],
            "abdc-bca": [],
            "abdc-cab": [],
            "abdc-cba": [],
            "acbd-abc": [],
            "acbd-acb": [],
            "acbd-bac": [],
            "acbd-bca": [],
            "acbd-cab": [],
            "acbd-cba": [],
            "acdb-abc": [],
            "acdb-acb": [],
            "acdb-bac": [],
            "acdb-bca": [],
            "acdb-cab": [],
            "acdb-cba": [],
            "adbc-abc": [],
            "adbc-acb": [],
            "adbc-bac": [],
            "adbc-bca": [],
            "adbc-cab": [],
            "adbc-cba": [],
            "adcb-abc": [],
            "adcb-acb": [],
            "adcb-bac": [],
            "adcb-bca": [],
            "adcb-cab": [],
            "adcb-cba": [],
            "bacd-abc": [],
            "bacd-acb": [],
            "bacd-bac": [],
            "bacd-bca": [],
            "bacd-cab": [],
            "bacd-cba": [],
            "badc-abc": [],
            "badc-acb": [],
            "badc-bac": [],
            "badc-bca": [],
            "badc-cab": [],
            "badc-cba": [],
            "bcad-abc": [],
            "bcad-acb": [],
            "bcad-bac": [],
            "bcad-bca": [],
            "bcad-cab": [],
            "bcad-cba": [],
            "bcda-abc": [],
            "bcda-acb": [],
            "bcda-bac": [],
            "bcda-bca": [],
            "bcda-cab": [],
            "bcda-cba": [],
            "bdac-abc": [],
            "bdac-acb": [],
            "bdac-bac": [],
            "bdac-bca": [],
            "bdac-cab": [],
            "bdac-cba": [],
            "bdca-abc": [],
            "bdca-acb": [],
            "bdca-bac": [],
            "bdca-bca": [],
            "bdca-cab": [],
            "bdca-cba": [],
            "cabd-abc": [],
            "cabd-acb": [],
            "cabd-bac": [],
            "cabd-bca": [],
            "cabd-cab": [],
            "cabd-cba": [],
            "cadb-abc": [],
            "cadb-acb": [],
            "cadb-bac": [],
            "cadb-bca": [],
            "cadb-cab": [],
            "cadb-cba": [],
            "cbad-abc": [],
            "cbad-acb": [],
            "cbad-bac": [],
            "cbad-bca": [],
            "cbad-cab": [],
            "cbad-cba": [],
            "cbda-abc": [],
            "cbda-acb": [],
            "cbda-bac": [],
            "cbda-bca": [],
            "cbda-cab": [],
            "cbda-cba": [],
            "cdab-abc": [],
            "cdab-acb": [],
            "cdab-bac": [],
            "cdab-bca": [],
            "cdab-cab": [],
            "cdab-cba": [],
            "cdba-abc": [],
            "cdba-acb": [],
            "cdba-bac": [],
            "cdba-bca": [],
            "cdba-cab": [],
            "cdba-cba": [],
            "dabc-abc": [],
            "dabc-acb": [],
            "dabc-bac": [],
            "dabc-bca": [],
            "dabc-cab": [],
            "dabc-cba": [],
            "dacb-abc": [],
            "dacb-acb": [],
            "dacb-bac": [],
            "dacb-bca": [],
            "dacb-cab": [],
            "dacb-cba": [],
            "dbac-abc": [],
            "dbac-acb": [],
            "dbac-bac": [],
            "dbac-bca": [],
            "dbac-cab": [],
            "dbac-cba": [],
            "dbca-abc": [],
            "dbca-acb": [],
            "dbca-bac": [],
            "dbca-bca": [],
            "dbca-cab": [],
            "dbca-cba": [],
            "dcab-abc": [],
            "dcab-acb": [],
            "dcab-bac": [],
            "dcab-bca": [],
            "dcab-cab": [],
            "dcab-cba": [],
            "dcba-abc": [],
            "dcba-acb": [],
            "dcba-bac": [],
            "dcba-bca": [],
            "dcba-cab": [],
            "dcba-cba": [],
        }
        for key in mapping:
            for val in value:
                if attribute[0:8] == "teammate":
                    mapping[key].append(
                        {
                            "teammate{}_weapon".format(
                                find_2nd(key, attribute[9]) - 5
                            ): val
                        }
                    )
                elif attribute[0:8] == "opponent":
                    mapping[key].append(
                        {
                            "opponent{}_weapon".format(
                                key.index(attribute[9]),
                            ): val
                        }
                    )
                else:
                    mapping[key].append({"player_weapon": val})
        battles = Battle.objects.none()
        for val in mapping.values():
            for query in val:
                battles = battles | Battle.objects.filter(**query)
        battles = battles.order_by("-time")
        return battles
