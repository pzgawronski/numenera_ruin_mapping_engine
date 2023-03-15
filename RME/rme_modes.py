from rme_rooms import *

MAPPING = {
    "Corridor": Corridor,
    "Chamber": Chamber,
    "Creature": Creature,
    "Explorers": Explorers,
    "Interstitial cavity": InterstitialCavity,
    "Accessway": Accessway,
    "Rupture": Rupture,
    "Shaft": Shaft,
    "Abhuman colony": AbhumanColony,
    "Integrated machine": IntegratedMachine,
    "Matter leak": MatterLeak,
    "Energy discharge": EnergyDischarge,
    "Weird event": WeirdEvent,
    "Vault": Vault,
    "Relic chamber": RelicChamber
}


def display_secondary(encounter: Generator):
    if encounter.secondary:
        encounter.secondary = rme_choice(encounter.secondary)
        encounter.display_name += f" IN {encounter.secondary.display_name}"
        encounter.type += f"\n{encounter.secondary.type}"


def format_cascade(rooms_dict: dict):
    formatted_rooms_string = ""
    for level in rooms_dict:
        for room in rooms_dict[level]:
            formatted_rooms_string += "\n" if level > 0 else ""
            formatted_rooms_string += f"{room[0]} {level}: {room[1]}"
    return formatted_rooms_string


def rme_choice(main_feat: str):
    new_choice = MAPPING[main_feat]()
    display_secondary(new_choice)
    return new_choice


def rme_random():
    new_encounter = generate_main()
    new_encounter_obj = rme_choice(new_encounter)
    return new_encounter_obj


def rme_cascade(x: int):
    rooms = {}
    counter = 0
    rooms[counter] = [("Seed", rme_random())]
    while counter < x:
        counter += 1
        rooms[counter] = []
        for room_tuple in rooms[counter-1]:
            for door in room_tuple[1].exits:
                next_room = rme_random()
                rooms[counter].append((door, next_room))
    return format_cascade(rooms)

# print(rme_cascade(3))
