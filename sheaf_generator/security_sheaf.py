###
# Security Sheaf
# Core Rulebook p.210
# Matrix p.115
# Description: As the Decker performs illegitimate actions on a host, the host system will begin to rack up a security tally
# At predetermined levels in the tally, or Trigger Steps, the host security will respond with IC or various alert stages.
###

from typing import Dict
from sheaf_generator.dice_roller import basic_roll
from sheaf_generator import matrix_constants as matrix
from sheaf_generator.ic_program import ICProgram, WhiteIC


def generate_sheaf(host_level: int, security_rating: int, has_nasty_surprises: bool) -> None:
    alert_level_table: Dict[int, str] = {
        0: matrix.NO_ALERT,
        1: matrix.PASSIVE_ALERT,
        2: matrix.ACTIVE_ALERT,
        3: matrix.SHUTDOWN
    }

    alert_level = 0  # 0 = No Alert, 1 = Passive, 2 = Active, 3 = Shutdown
    steps_since_last_alert = 0
    current_step = 0

    # Infinite Looping Failsafe Variables
    current_count = 0
    max_count = 100

    print("STARTING:")

    while alert_level < 3 and current_count < max_count:  # Has not yet reached Alert Level: Shutdown
        # Step 1: Trigger Step
        current_step += roll_trigger_step(host_level)  # Increment Step Counter
        sheaf_step = SheafStep(current_step)  # Generate a new Sheaf Step

        # Step 2: Alert Level
        alert_container = roll_alert_table(alert_level, steps_since_last_alert, False)
        generate_ic = True

        if alert_container.get_is_alert_step():
            steps_since_last_alert = 0
            alert_level += 1

            print(f"{current_step} -> Alert Status: {alert_level_table[alert_level]}")

            sheaf_step.set_title(alert_level_table[alert_level])

            print(f"{sheaf_step.get_title()}")

            # If A host is Blue or Green or has reach shutdown it won't generate more IC on an Alert Step
            if host_level <= 1 or alert_level == 3:
                generate_ic = False
            else:
                alert_container = roll_alert_table(alert_level, steps_since_last_alert, True)
        else:
            steps_since_last_alert += 1

        if generate_ic:
            sheaf_step.add_ic(process_ic(alert_container, security_rating))

        print(f"{current_step}: {sheaf_step.list_ic()}")

        # Infinite Loop Failsafe
        current_count += 1


def roll_trigger_step(host_level: int) -> int:
    base_step = sum(basic_roll(1, 3))

    # print(base_step)

    switch = {
        0: base_step + 4,
        1: base_step + 3,
        2: base_step + 2,
        3: base_step + 1
    }
    return switch.get(host_level, "Invalid Number")


class AlertContainer:
    def __init__(self, level_ic=None, category_ic=None, is_alert_step=False):
        self.level_ic = level_ic
        self.category_ic = category_ic
        self.is_alert_step = is_alert_step

    def get_level_ic(self):
        return self.level_ic

    def get_category_ic(self):
        return self.category_ic

    def get_is_alert_step(self):
        return self.is_alert_step


def roll_alert_table(alert_level: int, steps_since_last_alert: int, limit_to_ic: bool) -> AlertContainer:
    roll_result = sum(basic_roll(1, 6))

    final_results = roll_result if limit_to_ic else roll_result + steps_since_last_alert

    # print(f"Final Results: {final_results}")

    if alert_level == 0:
        if final_results in [1, 2, 3]:
            return AlertContainer(matrix.WHITE, matrix.REACTIVE)
        elif final_results in [4, 5]:
            return AlertContainer(matrix.WHITE, matrix.PROACTIVE)
        elif final_results in [6, 7]:
            return AlertContainer(matrix.GRAY, matrix.REACTIVE)
        else:
            return AlertContainer(is_alert_step=True)
    elif alert_level == 1:
        if final_results in [1, 2, 3]:
            return AlertContainer(matrix.WHITE, matrix.PROACTIVE)
        elif final_results in [4, 5]:
            return AlertContainer(matrix.GRAY, matrix.REACTIVE)
        elif final_results in [6, 7]:
            return AlertContainer(matrix.GRAY, matrix.PROACTIVE)
        else:
            return AlertContainer(is_alert_step=True)
    else:
        if final_results in [1, 2, 3]:
            return AlertContainer(matrix.GRAY, matrix.PROACTIVE)
        elif final_results in [4, 5]:
            return AlertContainer(matrix.WHITE, matrix.PROACTIVE)
        elif final_results in [6, 7]:
            return AlertContainer(matrix.BLACK, None)
        else:
            return AlertContainer(is_alert_step=True)


class SheafStep:
    def __init__(self, current_step):
        self.current_step = current_step
        self.title = ""
        self.ic_list = []
        self.is_construct = False
        self.is_party_cluster = False

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def add_ic(self, ic_program):
        self.ic_list.append(ic_program)

    def is_construct(self):
        return self.is_construct

    def set_construct(self, is_construct):
        self.is_construct = is_construct

    def is_party_cluster(self):
        return self.is_party_cluster

    def set_party_cluster(self, is_party_cluster):
        self.is_party_cluster = is_party_cluster

    def get_ic_list(self):
        return self.ic_list

    def list_ic(self):
        if len(self.ic_list) == 0:
            return ""
        elif len(self.ic_list) == 1:
            return str(self.ic_list[0])
        else:
            return str(self.ic_list)


def process_ic(alert_container: AlertContainer, host_level: int):
    level = alert_container.get_level_ic()
    if level == matrix.WHITE:
        return WhiteIC(alert_container.get_category_ic(), host_level)

