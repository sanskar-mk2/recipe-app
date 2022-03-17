import os
import json


def json_to_dict(file):
    with open(file, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    files = next(os.walk("./foods"))[2]
    arr = list()
    for file in files:
        arr.append(json_to_dict(f"./foods/{file}"))

    with open("./complete.json", "w") as f:
        json.dump(arr, f)
