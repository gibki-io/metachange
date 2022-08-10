import json, os
from pathlib import Path

for path in Path("metadata").iterdir():
    if path.is_file():
        address = Path(path).stem

        current_file = open(path, "r")
        new_file = open("build/"+address+".json", "w")
        metadata = json.load(current_file)

        metadata["creators"] = [
            {"address":"66CArwTsEvedcGYgV9vuYF92iRJisHm4WMfWxJviGasm","share":0,"verified":True},
            {"address":"BCJqqXatLeCKZtViBH5iFSQVMx6PnJeFQbSyQypwWuZM","share":81,"verified":False},
            {"address": "Uztzyg11P1wGBQfwbQTRAGB1zC2iV6vXthu3BRVjXGe", "share": 19, "verified": False},
        ]

        wrapper = {"mint_account": "", "nft_data": {}}

        wrapper["mint_account"] = address
        wrapper["nft_data"] = metadata

        json.dump(wrapper, new_file, indent=4)
        new_file.close()
        current_file.close()
        print(address + " Success")
