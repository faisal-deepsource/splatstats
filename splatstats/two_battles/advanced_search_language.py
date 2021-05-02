from django.utils.translation import gettext_lazy as _
import regex
from .models import Battle, Weapons, MainAbilities, SubAbilities, Stage, Clothes

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
    OR,
    AND,
    NOT,
    LPAREN,
    RPAREN,
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
    "OR",
    "AND",
    "NOT",
    "(",
    ")",
    "",
)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance."""
        return "Token({type}, {value})".format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

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
        if float(result) == int(result):
            return int(result)
        return float(result)

    def string(self):
        """Return a string consumed from the input."""
        result = ""
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        return result

    def attr(self):
        result = ""
        while self.current_char is not None and not self.current_char.isspace():
            result += self.current_char
            self.advance()
        return result

    def boolean(self):
        """Returns a boolean value consumed from the input."""
        result = ""
        while self.current_char is not None and not self.current_char.isspace():
            result += self.current_char
            self.advance()
        return result == "True" or result == "true"

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == "T" or self.current_char == "F":
                return Token(BOOL, self.boolean())

            if self.current_char == "A":
                self.advance()
                if self.current_char == "N":
                    self.advance()
                    if self.current_char == "D":
                        self.advance()
                        return Token(AND, "AND")
                    self.error()
                self.error()

            if self.current_char == "N":
                self.advance()
                if self.current_char == "O":
                    self.advance()
                    if self.current_char == "T":
                        self.advance()
                        return Token(NOT, "NOT")
                    self.error()
                self.error()

            if self.current_char == "O":
                self.advance()
                if self.current_char == "R":
                    self.advance()
                    return Token(OR, "OR")
                self.error()

            if self.current_char.isalpha():
                return Token(ATTR, self.attr())

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

            self.error()

        return Token(EOL, None)


def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


class Interpreter(object):
    """
    expr   : STRING (GREATERTHAN | GREATEREQUAL | LESSTHAN | LESSEQUAL | EQUAL) VALUE
    term   : (expr) | (LPAREN term (OR | AND) term RPAREN) | (NOT LPAREN term RPAREN)
    value  : INTEGER | FLOAT | STRING | BOOL
    """

    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        """term : (expr) | (LPAREN term (OR | AND) term RPAREN) | (NOT LPAREN term RPAREN) """
        if self.current_token.type is NOT:
            self.eat(NOT)
            self.eat(LPAREN)
            result = Battle.objects.all().difference(self.term())
            self.eat(RPAREN)
        elif self.current_token.type is LPAREN:
            self.eat(LPAREN)
            set_a = self.term()
            token = self.current_token
            if token.type == OR:
                self.eat(OR)
                result = set_a | self.term()
            elif token.type == AND:
                self.eat(AND)
                result = set_a & self.term()
            self.eat(RPAREN)
        else:
            result = self.expr()
        return result

    def value(self):
        """INTEGER | FLOAT | STRING | BOOL"""
        token = self.current_token
        self.eat(token.type)
        return token.value

    def expr(self):
        """expr   : STRING (GREATERTHAN | GREATEREQUAL | LESSTHAN | LESSEQUAL | EQUAL) VALUE"""
        attribute = self.value()
        if regex.search(
            "(rule)|(match_type)|(stage)|(win(_meter)?)|(has_disconnected_player)|(((my)|(other))_team_count)|((elapsed_)?time)|(tag_id)|(battle_number)|(((league)|(splatfest))_point)|(splatfest_title_after)|(player_x_power)|(((player)|(teammate_[a-c])|(opponent_[a-d]))_(((headgear)|(clothes)|(shoes))(_((sub[0-2])|(main)))?|(weapon)|(rank)|(level(_star)?)|(kills)|(deaths)|(assists)|(specials)|(game_paint_point)|(splatfest_title)|(name)|(splatnet_id)|(gender)|(species)))",
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
            self.eat(token.type)
            value = self.value()
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
                "((player)|(teammate_[a-c])|(opponent_[a-c]))_clothes", attribute
            ):
                value_a = [x for (x, y) in Clothes if y == value]
                if len(value_a) > 0:
                    value = value_a[0]
            if regex.search(
                "((teammate_[a-c])|(opponent_[a-d]))_[0-z_]*",
                attribute,
            ):
                for key in mapping:
                    if attribute[0:8] == "teammate":
                        mapping[key][
                            "{}{}{}()".format(
                                attribute[0:8],
                                find_2nd(key, attribute[9]) - 5,
                                attribute[10:],
                                switch[token.type],
                            )
                        ] = value
                    else:
                        mapping[key][
                            "{}{}{}{}".format(
                                attribute[0:8],
                                key.index(attribute[9]),
                                attribute[10:],
                                switch[token.type],
                            )
                        ] = value
            else:
                for key in mapping:
                    mapping[key][attribute + switch[token.type]] = value
            battles = Battle.objects.none()
            for key in mapping:
                battles = battles | Battle.objects.filter(**(mapping[key])).order_by(
                    "-time"
                )
            return battles
        self.error()
