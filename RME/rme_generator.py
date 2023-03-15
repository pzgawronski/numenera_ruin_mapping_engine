from rme_raw import RUIN_MAPPING_ENGINE
import random

POSSIBLE_VALUES = [10, 20, 100]


def _check_max(number, values):
    """
    :param number: value to be compared with possible maximum values
    :param values: list of possible maximum values
    :return: maximum possible value from the list
    Checks for the highest value in a given engine dictionary and returns one of the possible max values.
    """
    if number in values:
        return number
    else:
        for value in values:
            if number < value:
                number = value
        return number


def _engine_search(number, engine):
    """
    :param number: random integer within the maximal range of a given engine
    :param engine: an engine dict
    :return: a tuple with an existing key as an integer and the result from the engine dict as a string
    Checks if the rolled number exists in the engine; if not, checks the preceding values until it hits an existing key.
    Returns the value behind the found key from the engine dict.
    """
    engine = engine
    if number in engine:
        return engine[number]
    else:
        number -= 1
        return _engine_search(number, engine)


def _generate_result(engine):
    """
    :param engine: an engine dict
    :return: a tuple with an existing key as an integer and the result from the engine dict as a string
    Returns an existing key and its value from the corresponding engine dict as a tuple.
    """
    engine_dict = RUIN_MAPPING_ENGINE[engine]
    number_list = list(engine_dict.keys())
    number_max = max(number_list)
    true_max = _check_max(number_max, POSSIBLE_VALUES)
    number = random.randint(1, true_max)
    text = _engine_search(number, engine_dict)
    return number, text


def _generate_item(engine):
    """
    :param engine: an engine dict
    :return: value from the engine dict
    """
    item = _generate_result(engine)
    return item[1]


def generate_main():
    return _generate_item("MAIN FEATURE")


class Exit:

    def __init__(self, state="Exit"):
        self.state = state

    def __str__(self):
        if self.state == "Exit":
            return f"Normal exit"
        else:
            exit_string = f"{self.state.capitalize()} exit"
        return exit_string


class Generator:

    def __init__(self, engine: str, room=False):
        self.engine = engine
        self.display_name = engine
        self.description = ""
        self.exits = []
        self.generate_exits()
        if room:
            self.secondary = self.generate_item("SECONDARY FEATURE")
            self.display_name +=\
                f" IN {self.secondary.upper()}"

    def __str__(self):
        generator_string =\
            f"{self.display_name}\n\n" \
            f"# Description\n" \
            f"- {self.description}\n\n" \
            f"# Exits\n" \
            f"- {self.format_exits()}\n"
        return generator_string

    def format_exits(self):
        formatted_exits = []
        for raw_exit in self.exits:
            formatted_exits.append(str(raw_exit))
        if len(formatted_exits) == 0:
            return "No additional exits"
        elif formatted_exits:
            joined_exits = "\n- ".join(formatted_exits)
            return f"{joined_exits}"

    @staticmethod
    def generate_item(engine):
        """
        :param engine: an engine dict
        :return: value from the engine dict
        """
        item = _generate_result(engine)
        return item[1]

    def generate_exits(self):
        rolled_exits = _generate_item("EXIT")
        for rolled_exit in rolled_exits:
            if rolled_exit == "Again":
                self.generate_exits()
                continue
            self.exits.append(Exit(rolled_exit))

    def generate_feats(self):
        self.feats = []
        for i in range(1, 3):
            self.feats.append(_generate_item(f"CHAMBER {i}"))

    def replace_display(self, prename, postname):
        self.display_name = self.display_name.replace(f"{prename}", f"{postname}")

    def update_description(self):
        old_string = "1d10 x 100 feet (30 m)"
        new_string = f"{random.randint(1, 10)*30}m"
        new_display = self.description.replace(old_string, new_string)
        self.description = new_display


class Single(Generator):

    def __init__(self, engine: str, room=False):
        super().__init__(engine, room=room)
        self.type = _generate_item(self.engine)
        self.description = self.type
        self.update_description()


class Double(Generator):

    def __init__(self, engine: str, count=False, room=True, number=None):
        super().__init__(engine, room=room)
        self.type = _generate_item(f"{self.engine} TYPE")
        self.char = _generate_item(f"{self.engine} CHARACTERISTICS")
        self.count = count
        self.number = number
        self.description = \
            f"{self.number} {'counts' if self.count else None} of {self.type}\n" \
            f"- {self.char}"
        self.update_description()
