# see reference grammar langage_ebnf.txt
from types import BuiltinMethodType
import regex
from ...tools import get_size
from .models import (
    Battle,
    WeaponFamily,
    Clothes,
    Headgear,
    Shoes,
    WeaponSpecials,
    WeaponSubs,
    Weapons,
    Stage,
)
from django.db.models import Q


class QQ:
    def __sub__(self, other):
        return self & (~other)

    def __xor__(self, other):
        return (self - other) | (other - self)


Q.__bases__ += (QQ,)

(
    ATTR,
    ASSIGN,
    BUILTIN_FUNCT,
    USER_FUNCT,
    CONTROLFLOW,
    LPAREN,
    RPAREN,
    LBRACKET,
    RBRACKET,
    LSQUIGGLE,
    RSQUIGGLE,
    NEWLINE,
    COMMA,
    DOT,
    STRING,
    VAR,
    BOOL,
    INT,
    FLOAT,
    EOF,
    RETURN,
) = (
    "ATTR",
    ":=",
    "BUILTIN_FUNCT",
    "def",
    "CONTROLFLOW",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "NEWLINE",
    ",",
    ".",
    '"',
    "VAR",
    "False",
    "0",
    "0.0",
    "",
    "return",
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
    def error(str=""):
        raise Exception("Invalid character\n{}".format(str))

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

    def string(self):
        result = []
        while self.current_char is not None and self.current_char != '"':
            result.append(self.current_char)
            self.advance()
        self.advance()
        return Token(STRING, "".join(result))

    def attr_var_keyword(self):
        result = []
        while self.current_char is not None and (
            (self.current_char.isalpha() and self.current_char.islower())
            or self.current_char.isdigit()
            or self.current_char == "_"
        ):
            result.append(self.current_char)
            self.advance()
        value = "".join(result)
        if regex.search(
            "^((rule)|(match_type)|(stage)|(win(_meter)?)|(has_disconnected_player)|(((my)|(other))_team_count)|((elapsed_)?time)|(tag_id)|(battle_number)|(((league)|(splatfest))_point)|(splatfest_title_after)|(player_x_power)|(((player)|(teammate_[a-c])|(opponent_[a-d]))_(((headgear)|(clothes)|(shoes))(_((sub[0-2])|(main)))?|(weapon((_family)|(_sub)|(_special))?)|(rank)|(level(_star)?)|(kills)|(deaths)|(assists)|(specials)|(game_paint_point)|(splatfest_title)|(name)|(splatnet_id)|(gender)|(species))))$",
            value,
        ):
            return Token(ATTR, value)
        if regex.search(
            "^((g[et])|(l[et])|(eq)|(not)|(and)|(x?or)|(index)|(len))$", value
        ):
            return Token(BUILTIN_FUNCT, value)
        if regex.search("^((if)|(else)|(while))$", value):
            return Token(CONTROLFLOW, value)
        if regex.search("^def$", value):
            return Token(USER_FUNCT, value)
        if regex.search("^return$", value):
            return Token(RETURN, "return")
        return Token(VAR, value)

    def num(self, neg=False):
        result = []
        if neg:
            result.append("-")
        while self.current_char is not None and (
            self.current_char.isdigit() or self.current_char == "."
        ):
            result.append(self.current_char)
            self.advance()
        try:
            return Token(INT, int("".join(result)))
        except:
            return Token(FLOAT, float("".join(result)))

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
                    return Token(NEWLINE, "\r\n")
                return Token(NEWLINE, "\r")

            if self.current_char == "\n":
                self.advance()
                return Token(NEWLINE, "\n")

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.num()

            if self.current_char.isalpha() and self.current_char.islower():
                return self.attr_var_keyword()

            if self.current_char == "T":
                self.advance()
                if self.current_char == "r":
                    self.advance()
                    if self.current_char == "u":
                        self.advance()
                        if self.current_char == "e":
                            self.advance()
                            return Token(BOOL, True)
                self.error()

            if self.current_char == "F":
                self.advance()
                if self.current_char == "a":
                    self.advance()
                    if self.current_char == "l":
                        self.advance()
                        if self.current_char == "s":
                            self.advance()
                            if self.current_char == "e":
                                self.advance()
                                return Token(BOOL, False)
                self.error()

            if self.current_char == "+":
                self.advance()
                return Token(BUILTIN_FUNCT, "+")

            if self.current_char == "-":
                self.advance()
                if self.current_char.isdigit():
                    return self.num(True)
                return Token(BUILTIN_FUNCT, "-")

            if self.current_char == "*":
                self.advance()
                return Token(BUILTIN_FUNCT, "*")

            if self.current_char == "/":
                self.advance()
                return Token(BUILTIN_FUNCT, "/")

            if self.current_char == "(":
                self.advance()
                return Token(LPAREN, "(")

            if self.current_char == ")":
                self.advance()
                return Token(RPAREN, ")")

            if self.current_char == "[":
                self.advance()
                return Token(LBRACKET, "[")

            if self.current_char == "]":
                self.advance()
                return Token(RBRACKET, "]")

            if self.current_char == "{":
                self.advance()
                return Token(LSQUIGGLE, "{")

            if self.current_char == "}":
                self.advance()
                return Token(RSQUIGGLE, "}")

            if self.current_char == ",":
                self.advance()
                return Token(COMMA, ",")

            if self.current_char == ".":
                self.advance()
                return Token(DOT, ".")

            if self.current_char == '"':
                self.advance()
                return self.string()

            if self.current_char == ":":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(ASSIGN, ":=")
                self.error()

            self.error()
        return Token(EOF, None)


class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()
        self.vars = [
            {
                "weapons": [x for (x, y) in Weapons if x != "all"],
                "stages": [x for (x, y) in Stage if x != "all"],
                "clothes": [x for (x, y) in Clothes],
                "headgear": [x for (x, y) in Headgear],
                "shoes": [x for (x, y) in Shoes],
                "weapon_family": [x for (x, y) in WeaponFamily],
                "weapon_subs": [x for (x, y) in WeaponSubs],
                "weapon_specials": [x for (x, y) in WeaponSpecials],
            }
        ]
        self.switch_comp = {
            "gt": lambda a, b: a > b,
            "lt": lambda a, b: a < b,
            "ge": lambda a, b: a >= b,
            "le": lambda a, b: a <= b,
            "eq": lambda a, b: a == b,
        }
        self.switch_query = {
            "gt": "__gt",
            "lt": "__lt",
            "ge": "__gte",
            "le": "__lte",
            "eq": "",
        }
        self.switch_math = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.values = (
            BOOL,
            INT,
            FLOAT,
            STRING,
        )
        self.logical_bitwise_switch = {
            "and": lambda a, b: self.and_handler(a, b),
            "or": lambda a, b: self.or_handler(a, b),
            "xor": lambda a, b: self.xor_handler(a, b),
        }

    @staticmethod
    def error(str=""):
        raise Exception("Invalid syntax\n{}".format(str))

    def eat(self, token_type):
        """
        compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token,
        otherwise raise an exception.
        """
        # print(str(self.current_token.value) + " " + token_type)
        if self.current_token.type == token_type:
            if len(self.lexer.pos) > 0:
                self.current_token = self.lexer.get_next_token()
        else:
            self.error(
                "Tried to eat type {}, value {}, expecting type {}".format(
                    self.current_token.type, self.current_token.value, token_type
                )
            )

    def get_var(self, var_name, level=-1):
        if level == -1:
            for i in range(level, -len(self.vars) - 1, -1):
                if var_name in self.vars[i]:
                    return self.vars[i][var_name]
            return None
        return self.vars[level][var_name]

    def interpret(self):
        while self.current_token.type is not RETURN:
            self.line()
        q_obj = self.line()
        if isinstance(q_obj, dict):
            value = list(q_obj.values())[0]
            for val in list(q_obj.values())[1:]:
                value = value | val
            q_obj = value
        return Battle.objects.filter(q_obj).order_by("-time")

    def line(self, evaluate=True):
        value = None
        if self.current_token.type is CONTROLFLOW:
            value = self.control_flow_handler(evaluate)
        elif self.current_token.type is USER_FUNCT:
            self.def_handler(evaluate)
        elif self.current_token.type is VAR:
            var_name = self.current_token.value
            self.eat(VAR)
            if self.current_token.value is DOT:
                self.eat(DOT)
                self.eat(BUILTIN_FUNCT)
                self.eat(LPAREN)
                index = self.term(evaluate)
                self.eat(RPAREN)
                var_value = self.term(evaluate)
                self.get_var(var_name)[index] = var_value
            else:
                self.eat(ASSIGN)
                var_value = self.term(evaluate)
                self.set_var(var_name, var_value, evaluate)
        else:
            self.eat(RETURN)
            self.eat(LPAREN)
            value = self.term(evaluate)
            self.eat(RPAREN)
        if self.current_token.type is NEWLINE:
            self.eat(NEWLINE)
        return value

    def control_flow_handler(self, evaluate=True):
        if self.current_token.value == "if":
            return self.if_handler(evaluate)
        if self.current_token.value == "while":
            return self.while_handler(evaluate)
        self.error("Other control flow options not implemented yet.")

    def def_handler(self, evaluate=True):
        self.eat(USER_FUNCT)
        funct_name = self.current_token.value
        self.eat(VAR)
        params = {}
        self.eat(LPAREN)
        while self.current_token.type is not RPAREN:
            params[self.current_token.value] = None
            self.eat(VAR)
            if self.current_token.type is COMMA:
                self.eat(COMMA)
        self.eat(RPAREN)
        self.eat(LSQUIGGLE)
        pos = self.lexer.get_pos()
        self.eat(NEWLINE)
        self.set_var(funct_name, {"pos": pos, "params": params}, evaluate)
        while self.current_token.type is not RSQUIGGLE:
            self.line(False)
        self.eat(RSQUIGGLE)
        return None

    def set_var(self, var_name, var_value, evaluate=True):
        # print(str(var_name) + " " + str(var_value) + " " + str(evaluate))
        if evaluate:
            self.vars[-1][var_name] = var_value
            if get_size(self.vars) > 1000000:
                self.error("Variables are too large!")

    def if_handler(self, evaluate=True):
        self.eat(CONTROLFLOW)
        self.eat(LPAREN)
        value = self.term(evaluate)
        result = None
        self.eat(RPAREN)
        self.eat(LSQUIGGLE)
        self.eat(NEWLINE)
        if value:
            while self.current_token.type is not RSQUIGGLE:
                result = self.line(evaluate)
            self.eat(RSQUIGGLE)
            self.eat(CONTROLFLOW)
            self.eat(LSQUIGGLE)
            self.eat(NEWLINE)
            while self.current_token.type is not RSQUIGGLE:
                self.line(False)
        else:
            while self.current_token.type is not RSQUIGGLE:
                self.line(False)
            self.eat(RSQUIGGLE)
            self.eat(CONTROLFLOW)
            self.eat(LSQUIGGLE)
            self.eat(NEWLINE)
            while self.current_token.type is not RSQUIGGLE:
                result = self.line(evaluate)
        self.eat(RSQUIGGLE)
        return result

    def while_handler(self, evaluate=True):
        self.eat(CONTROLFLOW)
        start_pos = self.lexer.get_pos()
        self.eat(LPAREN)
        result = None
        while self.term(evaluate):
            curr_pos = self.lexer.get_pos()
            self.eat(RPAREN)
            self.lexer.push_pos(start_pos - 1)
            self.lexer.push_pos(curr_pos - 1)
            self.lexer.advance()
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
        return result

    def not_handler(self, evaluate=True):
        self.eat(BUILTIN_FUNCT)
        self.eat(LPAREN)
        to_negate = self.term(evaluate)
        if isinstance(to_negate, dict):
            result = {}
            for key, value in to_negate.items():
                result[key] = ~value
        elif isinstance(to_negate, bool):
            result = not to_negate
        elif isinstance(to_negate, int):
            result = ~to_negate
        elif isinstance(to_negate, Q):
            if to_negate == Q(pk__isnull=False):
                result = Q(pk__in=[])
            elif to_negate == Q(pk__in=[]):
                result = Q(pk__isnull=False)
            else:
                result = ~to_negate
        else:
            result = not to_negate
        self.eat(RPAREN)
        return result

    def logical_bitwise_handler(self, evaluate=True):
        logical_type = self.current_token.value
        self.eat(BUILTIN_FUNCT)
        self.eat(LPAREN)
        term_a = self.term(evaluate)
        self.eat(COMMA)
        term_b = self.term(evaluate)
        result = self.logical_bitwise_switch[logical_type](term_a, term_b)
        self.eat(RPAREN)
        return result

    def and_handler(self, term_a, term_b):
        if isinstance(term_a, dict) and isinstance(term_b, dict):
            result = {}
            for x_1, x_2 in term_a.items():
                for y_1, y_2 in term_b.items():
                    if len(x_1) == len(y_1) and x_1 == y_1:
                        result[x_1] = x_2 & y_2
                    elif len(x_1) > len(y_1):
                        if len(x_1) == 4:
                            result["{}-{}".format(x_1, y_1)] = x_2 & y_2
                        elif len(x_1) == 7:
                            if len(y_1) == 3 and x_1[5:] == y_1:
                                result[x_1] = x_2 & y_2
                            elif len(y_1) == 4 and x_1[0:4] == y_1:
                                result[x_1] = x_2 & y_2
                    elif len(x_1) < len(y_1):
                        if len(y_1) == 4:
                            result["{}-{}".format(y_1, x_1)] = x_2 & y_2
                        elif len(y_1) == 7:
                            if len(x_1) == 3 and y_1[5:] == x_1:
                                result[y_1] = x_2 & y_2
                            elif len(x_1) == 4 and y_1[0:4] == x_1:
                                result[y_1] = x_2 & y_2
        elif isinstance(term_a, dict) and isinstance(term_b, Q):
            result = {}
            for x, y in term_a.items():
                result[x] = y & term_b
        elif isinstance(term_a, Q) and isinstance(term_b, dict):
            result = {}
            for x, y in term_b.items():
                result[x] = y & term_a
        elif isinstance(term_a, bool) and isinstance(term_b, bool):
            result = term_a and term_b
        elif isinstance(term_a, Q) and isinstance(term_b, Q):
            if term_a == term_b or term_b == Q(pk__isnull=False):
                result = term_a
            elif term_a == Q(pk__isnull=False):
                result = term_b
            elif (
                term_a == (~term_b)
                or (~term_a) == term_b
                or term_a == Q(pk__in=[])
                or term_b == Q(pk__in=[])
            ):
                result = Q(pk__in=[])
            else:
                result = term_a & term_b
        elif isinstance(term_a, int) and isinstance(term_b, int):
            result = term_a & term_b
        else:
            result = term_a and term_b
        return result

    def or_handler(self, term_a, term_b):
        if isinstance(term_a, dict) and isinstance(term_b, dict):
            result = {}
            for x_1, x_2 in term_a.items():
                for y_1, y_2 in term_b.items():
                    if len(x_1) == len(y_1) and x_1 == y_1:
                        result[x_1] = x_2 | y_2
                    elif len(x_1) > len(y_1):
                        if len(x_1) == 4:
                            result["{}-{}".format(x_1, y_1)] = x_2 | y_2
                        elif len(x_1) == 7:
                            if len(y_1) == 3 and x_1[5:] == y_1:
                                result[x_1] = x_2 | y_2
                            elif len(y_1) == 4 and x_1[0:4] == y_1:
                                result[x_1] = x_2 | y_2
                    elif len(x_1) < len(y_1):
                        if len(y_1) == 4:
                            result["{}-{}".format(y_1, x_1)] = x_2 | y_2
                        elif len(y_1) == 7:
                            if len(x_1) == 3 and y_1[5:] == x_1:
                                result[y_1] = x_2 | y_2
                            elif len(x_1) == 4 and y_1[0:4] == x_1:
                                result[y_1] = x_2 | y_2
        elif isinstance(term_a, dict) and isinstance(term_b, Q):
            result = {}
            for x, y in term_a.items():
                result[x] = y | term_b
        elif isinstance(term_a, Q) and isinstance(term_b, dict):
            result = {}
            for x, y in term_b.items():
                result[x] = y | term_a
        elif isinstance(term_a, bool) and isinstance(term_b, bool):
            result = term_a or term_b
        elif isinstance(term_a, Q) and isinstance(term_b, Q):
            if term_a == term_b or term_b == Q(pk__in=[]):
                result = term_a
            elif term_a == Q(pk__in=[]):
                result = term_b
            elif (
                term_a == (~term_b)
                or (~term_a) == term_b
                or term_a == Q(pk__isnull=False)
                or term_b == Q(pk__isnull=False)
            ):
                result = Q(pk__isnull=False)
            else:
                result = term_a | term_b
        elif isinstance(term_a, int) and isinstance(term_b, int):
            result = term_a | term_b
        else:
            result = term_a or term_b
        return result

    def xor_handler(self, term_a, term_b):
        if isinstance(term_a, dict) and isinstance(term_b, dict):
            result = {}
            temp_a = list(term_a.values())[0]
            temp_b = list(term_b.values())[0]
            for x in list(term_a.values())[1:]:
                temp_a = temp_a | x
            for y in list(term_b.values())[1:]:
                temp_b = temp_b | y
            result = temp_a ^ temp_b
            print(result)
        elif isinstance(term_a, dict) and isinstance(term_b, Q):
            result = term_b
            temp = list(term_a.values())[0]
            for x in list(term_a.values())[1:]:
                temp = temp | x
            result = term_b ^ temp
        elif isinstance(term_a, Q) and isinstance(term_b, dict):
            result = term_a
            temp = list(term_b.values())[0]
            for x in list(term_b.values())[1:]:
                temp = temp | x
            result = term_a ^ temp
        elif isinstance(term_a, bool) and isinstance(term_b, bool):
            result = bool(term_a ^ term_b)
        elif isinstance(term_a, Q) and isinstance(term_b, Q):
            if term_a == term_b:
                result = Q(pk__in=[])
            elif term_a == Q(pk__isnull=False):
                return ~term_b
            elif term_b == Q(pk__isnull=False):
                return ~term_a
            elif term_a == Q(pk__in=[]):
                return term_b
            elif term_b == Q(pk__in=[]):
                return term_a
            elif term_a == (~term_b) or (~term_a) == term_b:
                return Q(pk__isnull=False)
            else:
                return term_a ^ term_b
        elif isinstance(term_a, int) and isinstance(term_b, int):
            result = term_a ^ term_b
        else:
            result = bool(bool(term_a) ^ bool(term_b))
        return result

    def len_handler(self, evaluate=True):
        self.eat(BUILTIN_FUNCT)
        self.eat(LPAREN)
        value = self.term(evaluate)
        if isinstance(value, dict):
            result = list(value.values())[0]
            for item in list(value.values())[1:]:
                result = result | item
            result = Battle.objects.filter(result).count()
        elif isinstance(value, Q):
            result = Battle.objects.filter(value).count()
        elif value is not None:
            result = len(value)
        else:
            result = 0
        self.eat(RPAREN)
        return result

    def comp_op_handler(self, evaluate=True):
        comp_type = self.current_token.value
        self.eat(BUILTIN_FUNCT)
        self.eat(LPAREN)
        term_a = self.term(evaluate)
        self.eat(COMMA)
        term_b = self.term(evaluate)
        result = False
        if isinstance(term_a, Token) and term_a.type is ATTR:
            if regex.search("^player_weapon_family$", term_a.value):
                value_a = [x for (x, y) in WeaponFamily if y == term_b]
                if len(value_a) > 0:
                    term_b = value_a[0]
                mapping = {}
                if isinstance(term_b, tuple):
                    mapping = {}
                    mapping[
                        "player_weapon{}".format(self.switch_query[comp_type])
                    ] = term_b[0]
                    result = Q(**mapping)
                    for val in term_b[1:]:
                        mapping = {}
                        mapping[
                            "player_weapon{}".format(self.switch_query[comp_type])
                        ] = val
                        result = result | Q(**mapping)
                else:
                    mapping[term_a.value + self.switch_query[comp_type]] = term_b
                    result = Q(**mapping)
            elif regex.search("^player_weapon$", term_a.value):
                value_a = [x for (x, y) in Weapons if y == term_b]
                if len(value_a) > 0:
                    term_b = value_a[0]
                    mapping = {}
                    mapping[
                        "player_weapon{}".format(self.switch_query[comp_type])
                    ] = term_b
                    result = Q(**mapping)
            else:
                if isinstance(term_b, tuple):
                    mapping = {}
                    mapping[term_a.value + self.switch_query[comp_type]] = term_b[0]
                    result = Q(**mapping)
                    for val in term_b[1:]:
                        mapping = {}
                        mapping[term_a.value + self.switch_query[comp_type]] = val
                        result = result | Q(**mapping)
                else:
                    mapping = {}
                    mapping[term_a.value + self.switch_query[comp_type]] = term_b
                    result = Q(**mapping)
        elif isinstance(term_a, dict):
            if regex.search("^teammate[0-2]_weapon_family$", list(term_a.values())[0]):
                value_a = [x for (x, y) in WeaponFamily if y == term_b]
                if len(value_a) > 0:
                    term_b = value_a[0]
                result = {}
                for key, value in term_a.items():
                    if isinstance(term_b, tuple):
                        mapping = {}
                        mapping[
                            "teammate{}_weapon{}".format(
                                value[8], self.switch_query[comp_type]
                            )
                        ] = term_b[0]
                        result[key] = Q(**mapping)
                        for val in term_b[1:]:
                            mapping = {}
                            mapping[
                                "teammate{}_weapon{}".format(
                                    value[8], self.switch_query[comp_type]
                                )
                            ] = val
                            result[key] = result[key] | Q(**mapping)
                    else:
                        mapping = {}
                        mapping[
                            "teammate{}_weapon{}".format(
                                value[8], self.switch_query[comp_type]
                            )
                        ] = term_b
                        result[key] = Q(**mapping)
            elif regex.search(
                "^opponent[0-3]_weapon_family$", list(term_a.values())[0]
            ):
                value_a = [x for (x, y) in WeaponFamily if y == term_b]
                if len(value_a) > 0:
                    term_b = value_a[0]
                result = {}
                for key, value in term_a.items():
                    if isinstance(term_b, tuple):
                        mapping = {}
                        mapping[
                            "opponent{}_weapon{}".format(
                                value[8], self.switch_query[comp_type]
                            )
                        ] = term_b[0]
                        result[key] = Q(**mapping)
                        for val in term_b[1:]:
                            mapping = {}
                            mapping[
                                "opponent{}_weapon{}".format(
                                    value[8], self.switch_query[comp_type]
                                )
                            ] = val
                            result[key] = result[key] | Q(**mapping)
                    else:
                        mapping = {}
                        mapping[
                            "opponent{}_weapon{}".format(
                                value[8], self.switch_query[comp_type]
                            )
                        ] = term_b
                        result[key] = Q(**mapping)
            elif regex.search("^teammate[0-2]_weapon$", list(term_a.values())[0]):
                value_a = [x for (x, y) in Weapons if y == term_b]
                result = {}
                if len(value_a) > 0:
                    term_b = value_a[0]
                for key, value in term_a.items():
                    mapping = {}
                    mapping[
                        "teammate{}_weapon{}".format(
                            value[8], self.switch_query[comp_type]
                        )
                    ] = term_b
                    result[key] = Q(**mapping)
            elif regex.search("^opponent[0-3]_weapon$", list(term_a.values())[0]):
                value_a = [x for (x, y) in Weapons if y == term_b]
                result = {}
                if len(value_a) > 0:
                    term_b = value_a[0]
                for key, value in term_a.items():
                    mapping = {}
                    mapping[
                        "opponent{}_weapon{}".format(
                            value[8], self.switch_query[comp_type]
                        )
                    ] = term_b
                    result[key] = Q(**mapping)
            else:
                mapping = {}
                result = {}
                for key, value in term_a.items():
                    if isinstance(term_b, tuple):
                        mapping = {}
                        mapping[value + self.switch_query[comp_type]] = term_b[0]
                        result[key] = Q(**mapping)
                        for val in term_b[1:]:
                            mapping = {}
                            mapping[value + self.switch_query[comp_type]] = val
                            result[key] = result[key] | Q(**mapping)
                    else:
                        mapping[value + self.switch_query[comp_type]] = term_b
                        result[key] = Q(**mapping)
        elif term_a is not None and term_b is not None:
            result = self.switch_comp[comp_type](term_a, term_b)
        self.eat(RPAREN)
        return result

    def math_handler(self, evaluate=True):
        math_type = self.current_token.value
        self.eat(BUILTIN_FUNCT)
        self.eat(LPAREN)
        term_a = self.term(evaluate)
        self.eat(COMMA)
        term_b = self.term(evaluate)
        result = 0
        if math_type == "-" and isinstance(term_a, Q) and isinstance(term_b, Q):
            if term_b == Q(pk__id=[]):
                result = term_a
            else:
                result = term_a - term_b
        elif evaluate:
            result = self.switch_math[math_type](term_a, term_b)
        self.eat(RPAREN)
        return result

    def call_handler(self, func_name, evaluate=True):
        self.eat(LPAREN)
        params = self.get_var(func_name, 0)["params"].copy()
        i = 0
        while self.current_token.type is not RPAREN:
            params[list(params)[i]] = self.term(evaluate)
            if self.current_token.type is COMMA:
                self.eat(COMMA)
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
            self.lexer.pop_pos()
            self.eat(RSQUIGGLE)
            self.eat(NEWLINE)
        return result

    def term(self, evaluate=True):
        if self.current_token.type == BUILTIN_FUNCT:
            if self.current_token.value == "not":
                return self.not_handler(evaluate)
            if self.current_token.value in self.logical_bitwise_switch:
                return self.logical_bitwise_handler(evaluate)
            if self.current_token.value in self.switch_comp:
                return self.comp_op_handler(evaluate)
            if self.current_token.value == "len":
                return self.len_handler(evaluate)
            if self.current_token.value in self.switch_math:
                return self.math_handler(evaluate)
        if self.current_token.type in self.values:
            result = self.current_token.value
            self.eat(self.current_token.type)
            return result
        if self.current_token.type is ATTR:
            token = self.current_token
            self.eat(ATTR)
            if regex.search("^teammate_[a-c]", token.value):
                result = {
                    "abc": None,
                    "acb": None,
                    "bac": None,
                    "bca": None,
                    "cab": None,
                    "cba": None,
                }
                for key in result:
                    result[key] = "".join(
                        ["teammate", str(key.index(token.value[9])), token.value[10:]]
                    )
            elif regex.search("^opponent_[a-c]", token.value):
                result = {
                    "abcd": None,
                    "abdc": None,
                    "acbd": None,
                    "acdb": None,
                    "adbc": None,
                    "adcb": None,
                    "bacd": None,
                    "badc": None,
                    "bcad": None,
                    "bcda": None,
                    "bdac": None,
                    "bdca": None,
                    "cabd": None,
                    "cadb": None,
                    "cbad": None,
                    "cbda": None,
                    "cdab": None,
                    "cdba": None,
                }
                for key in result:
                    result[key] = "".join(
                        ["opponent", str(key.index(token.value[9])), token.value[10:]]
                    )
            else:
                result = token
            return result
        if self.current_token.type is LBRACKET:
            result = []
            while self.current_token.type is not RBRACKET:
                result.append(self.term(evaluate))
                if self.current_token.type is COMMA:
                    self.eat(COMMA)
            self.eat(RBRACKET)
            return result
        if self.current_token.type is VAR:
            var_name = self.current_token.value
            self.eat(VAR)
            if self.current_token.type is DOT:
                self.eat(DOT)
                self.eat(BUILTIN_FUNCT)
                self.eat(LPAREN)
                index = self.term(evaluate)
                self.eat(RPAREN)
                return self.get_var(var_name)[index]
            if self.current_token.type is LPAREN:
                return self.call_handler(var_name, evaluate)
            return self.get_var(var_name)
