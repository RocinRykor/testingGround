"""
IC Programs
Core Rulebook p.212
Matrix p.103

Intrusion Countermeasures, or IC (Pronounced as ICE), refers to autonomous system programs on matrix hosts
IC can range from harmless, meant to delay or simply survey the decker and their actions, to absolutely lethal
IC Levels: WHITE IC, GRAY IC, BLACK IC
"""

from sheaf_generator.dice_roller import basic_roll
from sheaf_generator import matrix_constants as matrix


# Super Class
class ICProgram:
    def __int__(self, category, system_security_value):
        self.category = category
        self.system_security_value = system_security_value

    def __str__(self):
        # TODO 1-30-23 Stopping Point: Implement rest of IC classes
        return "IC"

# Subclasses
def roll_reactive_white():
    roll = basic_roll()

    if roll < 3:
        return matrix.PROBE
    elif roll < 6:
        return matrix.TRACE
    elif roll == 6:
        return matrix.TAR_BABY
    else:
        Exception(f"Unexpected Value: {roll}")


class WhiteIC(ICProgram):
    pass
