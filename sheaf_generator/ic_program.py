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


def roll_crippler_ripper() -> str:
    """
    The roll_crippler_ripper function rolls a d6 and returns the result as a string.\n
    If the roll 1 or 2, it returns BOD.\n
    If the roll is 3, it returns EVASION.\n
    If the roll is 4 or 5, it returns MASKING.\n
    Otherwise (roll == 6), it returns SENSOR.

    :return: A string
    :doc-author: Rocin
    """
    roll = sum(basic_roll())

    if roll <= 2:
        return matrix.BOD
    elif roll == 3:
        return matrix.EVASION
    elif 4 <= roll <= 5:
        return matrix.MASKING
    elif roll == 6:
        return matrix.SENSOR
    else:
        Exception(f"Unexpected Value: {roll}")


def roll_psychotropic() -> str:
    """
    The roll_psychotropic function rolls a d6 and returns the result as a string.\n
    If the roll 1 or 2, it returns CYBERPHOBIA.\n
    If the roll is 3, it returns FRENZY.\n
    If the roll is 4, it returns JUDAS.\n
    Otherwise, if the roll is a 5 or 6, it returns POSITIVE_CONDITIONING.

    :return: A string
    :doc-author: Rocin
    """
    roll = sum(basic_roll())

    if roll <= 2:
        return matrix.CYBERPHOBIA
    elif roll == 3:
        return matrix.FRENZY
    elif roll == 4:
        return matrix.JUDAS
    elif 5 <= roll <= 6:
        return matrix.POSITIVE_CONDITIONING
    else:
        Exception(f"Unexpected Value: {roll}")


def ic_rating_table(i: int, i1: int, i2: int, i3: int) -> int:
    """
    The ic_rating_table function takes in four integers, and returns the appropriate integer based on a roll of 2d6.
    The first argument is the lowest possible value that can be returned, and each subsequent argument represents an increasing
    difficulty to achieve.

    :param i: The lowest IC rating possible, returned by a 2d6 roll of 5 or less
    :param i1: The second-lowest IC rating possible, returned by a 2d6 roll of 6 to 8
    :param i2: The third-lowest IC rating possible, returned by a 2d6 roll of 9 to 11
    :param i3: Highest value IC Rating, returned by a 2d6 roll of 12
    :return: An int value based on the roll of 2d6
    :doc-author: Rocin
    """
    roll = sum(basic_roll(2, 6))
    if roll <= 5:
        return i
    elif 6 <= roll <= 8:
        return i1
    elif 9 <= roll <= 11:
        return i2
    elif roll == 12:
        return i3
    else:
        Exception(f"Unexpected Value: {roll}")


class ICProgram:
    def __init__(self, ic_level_color: str = matrix.WHITE, ic_category: str = None):
        self.ic_level_color = ic_level_color
        self.ic_category = ic_category
        self.ic_type = None
        self.ic_rating = 1
        self.ic_options = []

    def process_ic(self, system_security_rating: int):
        """
        The process_ic function is used to generate the type of IC that will be rolled for a given system.
        The function takes in the security rating of the system and uses it to determine what color IC will be rolled.
        Then, using that color, it rolls an appropriate number of dice and adds them together to get an overall IC rating.

        :param self: Reference the object that is being created
        :param system_security_rating:int: The security rating of the system, determines final rating of the IC
        :return: The value of self
        :doc-author: Rocin
        """
        # step 1: Generate IC TYPE and any targeted Systems
        if self.ic_level_color == matrix.WHITE:
            self.roll_white_ic_type()
        elif self.ic_level_color == matrix.GRAY:
            self.roll_gray_ic_type()
        else:
            self.roll_black_ic_type()

        # Step 2: Determine IC Rating
        self.roll_ic_rating(system_security_rating)

        return self

    def roll_white_ic_type(self):
        """
        The roll_white_ic_type function is used to determine the type of IC that will be generated. Specific to White IC
        The function takes no arguments and returns a string containing the name of the IC type.
        If an error occurs, it raises an Exception with a message detailing what went wrong.

        :param self: Refer to the object itself
        :return: A string that represents the type of ic
        :doc-author: Rocin
        """
        if self.ic_category == matrix.REACTIVE:
            roll = sum(basic_roll())

            if roll <= 2:
                self.ic_type = matrix.PROBE
            elif 3 <= roll <= 5:
                self.ic_type = matrix.TRACE
            elif roll == 6:
                self.ic_type = matrix.TAR_BABY
            else:
                Exception(f"Unexpected Value: {roll}")
        else:
            roll = sum(basic_roll(2, 6))

            if roll <= 5:
                self.ic_type = f"{roll_crippler_ripper()}-{matrix.CRIPPLER}"
            elif 6 <= roll <= 8:
                self.ic_type = matrix.KILLER
            elif 9 <= roll <= 11:
                self.ic_type = matrix.SCOUT
            elif roll == 12:
                self.ic_type = matrix.CONSTRUCT
            else:
                Exception(f"Unexpected Value: {roll}")

    def roll_gray_ic_type(self):
        """
        The roll_white_ic_type function is used to determine the type of IC that will be generated. Specific to Gray IC
        The function takes no arguments and returns a string containing the name of the IC type.
        If an error occurs, it raises an Exception with a message detailing what went wrong.

        :param self: Refer to the object itself
        :return: A string that represents the type of ic
        :doc-author: Rocin
        """
        if self.ic_category == matrix.REACTIVE:
            roll = sum(basic_roll())

            if roll <= 2:
                self.ic_type = matrix.TAR_PIT
            elif roll == 3:
                self.ic_type = f"{matrix.TRACE} /w {matrix.TRAP}"
            elif roll == 4:
                self.ic_type = f"{matrix.PROBE} /w {matrix.TRAP}"
            elif roll == 5:
                self.ic_type = f"{matrix.SCOUT} /w {matrix.TRAP}"
            elif roll == 6:
                self.ic_type = matrix.CONSTRUCT
            else:
                Exception(f"Unexpected Value: {roll}")
        else:
            roll = sum(basic_roll(2, 6))

            if roll <= 5:
                self.ic_type = f"{roll_crippler_ripper()}-{matrix.RIPPER}"
            elif 6 <= roll <= 8:
                self.ic_type = matrix.BLASTER
            elif 9 <= roll <= 11:
                self.ic_type = matrix.SPARKY
            elif roll == 12:
                self.ic_type = matrix.CONSTRUCT
            else:
                Exception(f"Unexpected Value: {roll}")

    def roll_black_ic_type(self):
        """
        The roll_white_ic_type function is used to determine the type of IC that will be generated. Specific to Black IC
        The function takes no arguments and returns a string containing the name of the IC type.
        If an error occurs, it raises an Exception with a message detailing what went wrong.

        :param self: Refer to the object itself
        :return: A string that represents the type of ic
        :doc-author: Rocin
        """
        roll = sum(basic_roll(2, 6))

        if roll <= 4:
            self.ic_type = f"{roll_psychotropic()}-{matrix.PSYCHOTROPIC}"
        elif 5 <= roll <= 7:
            self.ic_type = matrix.LETHAL
        elif 8 <= roll <= 10:
            self.ic_type = matrix.NON_LETHAL
        elif roll == 11:
            self.ic_type = matrix.CEREBROPATHIC
        elif roll == 12:
            self.ic_type = matrix.CONSTRUCT
        else:
            Exception(f"Unexpected Value: {roll}")

    def roll_ic_rating(self, system_security_rating: int):
        """
        The roll_ic_rating function takes a system's security rating and uses it to determine the appropriate table for rolling the IC Rating.\n
        The ICs Rating is then determined by calling the ic_rating_table function.

        :param self: Refer to the object itself
        :param system_security_rating: System Security Rating, determines the final IC Rating
        :doc-author: Rocin
        """
        if system_security_rating <= 4:
            self.ic_rating = ic_rating_table(4, 5, 6, 7)
        if 5 <= system_security_rating <= 7:
            self.ic_rating = ic_rating_table(5, 7, 9, 10)
        if 8 <= system_security_rating <= 10:
            self.ic_rating = ic_rating_table(6, 8, 10, 12)
        else:
            self.ic_rating = ic_rating_table(8, 10, 11, 12)

    def __str__(self):
        # Verbose
        # return f"{self.ic_category} {self.ic_level_color} -> {self.ic_type} - {self.ic_rating}"

        # Basic
        return f"{self.ic_type}-{self.ic_rating}"
