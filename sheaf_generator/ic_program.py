"""
IC Programs
Core Rulebook p.212
Matrix p.103

Intrusion Countermeasures, or IC (Pronounced as ICE), refers to autonomous system programs on matrix hosts
IC can range from harmless, meant to delay or simply survey the decker and their actions, to absolutely lethal
IC Levels: WHITE IC, GRAY IC, BLACK IC

TODO LIST
1-30-23 Stopping Point: Implement rest of IC classes
1-31-23 Stopping Point: Progress made on Super Class, WhiteIC needs to update its type and rating, then need to start working on Gray and Black IC
"""
from sheaf_generator.dice_roller import basic_roll
from sheaf_generator import matrix_constants as matrix


# Super Class
class ICProgram:
    ic_category = "NONE"
    ic_level_color = matrix.WHITE
    ic_type = "NONE"
    ic_rating = 1
    ic_options = []

    def __init__(self, ic_category: str = "NO CATEGORY SELECTED", system_security_value: int = -1):
        self.ic_category = ic_category
        self.system_security_value = system_security_value

    def get_ic_category(self) -> str:
        return self.ic_category

    def get_system_security_value(self) -> int:
        return self.system_security_value

    def get_ic_type(self):
        return self.ic_type

    def set_ic_type(self, ic_type):
        self.ic_type = ic_type

    def get_ic_level_color(self):
        return self.ic_level_color

    def set_ic_level_color(self, ic_level_color):
        self.ic_level_color = ic_level_color

    def __str__(self):
        return f"{self.ic_category} {self.ic_level_color} -> {self.ic_options} {self.ic_type} - {self.ic_rating}"


def roll_crippler_ripper():
    roll = basic_roll()


# Subclasses
class WhiteIC(ICProgram):
    ic_level = matrix.WHITE


def roll_reactive_white():
    roll = basic_roll()

    print("Rolling Reactive IC")

    if roll <= 2:
        return matrix.PROBE
    elif 3 <= roll <= 5:
        return matrix.TRACE
    elif roll == 6:
        return matrix.TAR_BABY
    else:
        Exception(f"Unexpected Value: {roll}")


def roll_proactive_white():
    roll = sum(basic_roll(2, 6))

    if roll <= 5:
        return f"{roll_crippler_ripper()} - {matrix.CRIPPLER}"
    elif 6 <= roll <= 8:
        return matrix.KILLER
    elif 9 <= roll <= 11:
        return matrix.SCOUT
    elif roll == 12:
        return matrix.CONSTRUCT
    else:
        Exception(f"Unexpected Value: {roll}")
