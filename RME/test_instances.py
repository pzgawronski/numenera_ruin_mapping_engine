from rme_rooms import *

CLASSES = [
    Chamber,
    AbhumanColony,
    Accessway,
    Corridor,
    Creature,
    EnergyDischarge,
    Explorers,
    IntegratedMachine,
    InterstitialCavity,
    MatterLeak,
    RelicChamber,
    Rupture,
    Shaft,
    Vault,
    WeirdEvent]

for x in CLASSES:
    new_instance = x()
    print(new_instance)
