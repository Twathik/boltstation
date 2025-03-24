import re


def format_string(input_string):
    # Use regular expression to replace all non-alphanumeric characters (including spaces) with '_'
    result = re.sub(r"[^a-zA-Z0-9]", "_", input_string)
    return result
