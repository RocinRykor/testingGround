"""
IC Programs
Core Rulebook p.212
Matrix p.103

Intrusion Countermeasures, or IC (Pronounced as ICE), refers to autonomous system programs on matrix hosts
IC can range from harmless, meant to delay or simply survey the decker and their actions, to absolutely lethal
IC Levels: WHITE IC, GRAY IC, BLACK IC
"""


class ICProgram:
    def __int__(self, category, system_security_value):
        self.category = category
        self.system_security_value = system_security_value
