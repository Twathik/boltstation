import re


# Function to check if the string is in 'rgb(r,g,b)' format and convert it to hex
def rgb_to_hex_if_rgb(rgb_str):
    # Regular expression to check if the string is in 'rgb(r,g,b)' format
    rgb_pattern = r"^rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$"

    # If the string matches the pattern, convert it to hex
    if re.match(rgb_pattern, rgb_str):
        rgb_values = [int(value) for value in rgb_str[4:-1].split(",")]
        hex_value = "#" + "".join([f"{value:02x}" for value in rgb_values])
        return hex_value
    else:
        return rgb_str
