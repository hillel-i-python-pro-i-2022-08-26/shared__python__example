import json

from settings.paths import FILES_PATH


# Note: pydantic


def main():
    path = FILES_PATH.joinpath("example.txt")
    path.write_text("Hello")
    output = path.read_text()
    # ----
    path_to_json = FILES_PATH.joinpath("example.json")

    my_dict = {
        "name": "Alex",
        "age": 30,
        "something": None,
    }
    my_dict_as_json_str = json.dumps(my_dict, indent=2)
    path_to_json.write_text(my_dict_as_json_str)
    read_json = path_to_json.read_text()
    new_dict = json.loads(read_json)
    # ---

    print()


if __name__ == "__main__":
    main()
