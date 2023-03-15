import os, csv


def convert_filename(filename: str):
    name_capitals = filename.upper()
    name_split = name_capitals.split('.')
    name_split_dot = name_split[0]
    return name_split_dot


raw_files_directory = r'../RME_dicts'
raw_files = os.listdir(raw_files_directory)[0:-1]
RUIN_MAPPING_ENGINE = {}

for raw_file in raw_files:
    file_name = convert_filename(raw_file)
    engine_dict = {}
    with open(f'{raw_files_directory}/{raw_file}', newline='') as csv_file:
        raw_file = csv.reader(csv_file, delimiter=',')

        for row in raw_file:
            index_raw = row[0]
            index = int(index_raw)
            text = row[1]
            engine_dict[index] = text

    RUIN_MAPPING_ENGINE[file_name] = engine_dict

RUIN_MAPPING_ENGINE["EXIT"] = {
    1: [],
    5: ["Exit"],
    13: ["Sealed"],
    15: ["Exit", "Exit"],
    16: ["Exit", "Sealed"],
    17: ["Exit", "Exit", "Sealed"],
    18: ["Sealed", "Sealed"],
    19: ["Trapped", "Again"],
    20: ["Hidden", "Again"],
}

# print(RUIN_MAPPING_ENGINE.keys())
