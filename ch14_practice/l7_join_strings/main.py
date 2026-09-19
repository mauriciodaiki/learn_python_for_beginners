def join_strings(strings: list[str]) -> str:
    joined_string: str = ""
    for string in strings:
        joined_string += string + ","
    return joined_string[:-1]
