# json can be used to save dictionaries. It can be used for small db or for config files
import json
from typing import Any

with open("folder_1/myjson.json", "w") as f:
    # Create a dictionary
    statistics: dict[Any] = {
        "Health Point" : 80,
        "Attack" : {"Base" : 2, "Effects" : -1, "Equipment" : 2, "Other" : 0},
        "Defense" : [2, 0.0]
    }

    # This allows to save the content of the dictionary "statistics" into "folder_1/myjson.json" (named "f") 
    json.dump(statistics, f, indent=4)