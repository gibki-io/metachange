import json, os
from pathlib import Path

for path in Path("metadata").iterdir():
    if path.is_file():
        address = Path(path).stem

        current_file = open(path, "r")
        new_file = open("build/"+name+".json", "w")
        metadata = json.load(current_file)

        # Make changes to metadata
        # e.g. Change Creators
        # j["creators"] = [{"address": "FcCp7iSjaoY2R7tMtp4Ww8m4kWdrDx9FPWXGPfvQNEdP","verified": false,"share": 100}]

        wrapper = {"mint_account": "", "nft_data": {}}

        wrapper["mint_account"] = address
        wrapper["nft_data"] = metadata

        json.dump(wrapper, new_file, indent=4)
        new_file.close()
        current_file.close()
        print(name + " Success")
