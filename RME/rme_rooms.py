from rme_generator import *
import random


class Chamber(Generator):

    def __init__(self):
        super().__init__("CHAMBER")
        self.generate_feats()
        self.shape = self.generate_item("ROOM SHAPE")
        self.size = self.generate_item("ROOM SIZE")
        self.display_name += f" ({self.size}, {self.shape})"
        self.description = "\n- ".join(self.feats)


class AbhumanColony(Double):

    def __init__(self):
        super().__init__("ABHUMAN", count=True, room=True, number=8 + random.randint(9, 28))
        self.replace_display("ABHUMAN", "ABHUMAN COLONY")


class Accessway(Single):

    def __init__(self):
        super().__init__("ACCESSWAY")


class Corridor(Single):

    def __init__(self):
        super().__init__("CORRIDOR")
        self.reroll_corridor()
        self.description = self.type

    def _new_corridor(self):
        new_corridor = Corridor()
        for corridor_exit in new_corridor.exits:
            self.exits.append(corridor_exit)
        return new_corridor

    def reroll_corridor(self):
        if "roll again" in self.type:
            reroll = self._new_corridor()
            formatted_reroll = reroll.type.replace("Passage ", "then ")
            self.type = self.type.replace("roll again", formatted_reroll)
        elif "intersection" in self.type:
            split = []
            if "T intersection" in self.type:
                split = ["Left", "Right"]
            elif "X intersection" in self.type:
                split = ["Left", "Ahead", "Right"]
            for path in split:
                reroll = self._new_corridor()
                self.type += f"\n- {path} path: {reroll.type} ({reroll.format_exits()})"


class Creature(Single):

    def __init__(self):
        super().__init__("CREATURE", room=True)


class EnergyDischarge(Single):

    def __init__(self):
        super().__init__("ENERGY DISCHARGE", room=True)


class Explorers(Double):

    def __init__(self):
        super().__init__("EXPLORER", count=True, room=True, number=random.randint(2, 7))


class IntegratedMachine(Single):

    def __init__(self):
        super().__init__("INTEGRATED MACHINE", room=True)


class InterstitialCavity(Single):

    def __init__(self):
        super().__init__("INTERSTITIAL CAVITY")


class MatterLeak(Single):

    def __init__(self):
        super().__init__("MATTER LEAK", room=True)


class RelicChamber(Double):

    def __init__(self):
        super().__init__("RELIC")
        self.replace_display("RELIC", "RELIC CHAMBER")
        self.description = f"The {self.type} of {self.char}"


class Rupture(Single):

    def __init__(self):
        super().__init__("RUPTURE")


class Shaft(Single):

    def __init__(self):
        super().__init__("SHAFT")


class Vault(Single):

    def __init__(self):
        super().__init__("VAULT")


class WeirdEvent(Single):

    def __init__(self):
        super().__init__("WEIRD EVENT")
