from typing import List

from pprintpp import pprint


def format_lists(data: List[dict]) -> List[dict]:
    formatted_data: List[dict] = []
    for node_index, node in enumerate(data):
        append = True

        if "type" in node:

            if node["type"] == "p":
                if not "indent" in node:
                    node["indent"] = None
                if not "listStyleType" in node:
                    node["listStyleType"] = None
                else:
                    if node["listStyleType"] == "todo":
                        if node["checked"] == True:
                            children = []
                            for child in node["children"]:
                                children.append(
                                    {
                                        **child,
                                        "strikethrough": True,
                                        "color": "#475569",
                                    }
                                )
                            node["children"] = children
                            pass

                if node["children"][0] == {"text": ""}:
                    if node_index > 0:
                        if not data[node_index - 1]["children"][0] == {"text": ""}:
                            append = False

        if "AIgenerated" in node:
            if node["AIgenerated"] == True:
                append = False

        if append == True:
            formatted_data.append(node)

    formatted_data.append(
        {
            "type": "p",
            "indent": None,
            "listStyleType": None,
            "children": [{"text": ""}],
        }
    )

    new_data: List[dict] = []
    indent_level = 0
    list_type: dict = {}
    opened_list = False

    for node in formatted_data:
        if "type" in node:
            if node["type"] == "p":
                if not node["indent"] == None and (
                    node["listStyleType"] == "disc"
                    or node["listStyleType"] == "decimal"
                ):

                    if not opened_list:
                        new_data.append(
                            {
                                "type": (
                                    "begin_itemize"
                                    if node["listStyleType"] == "disc"
                                    else "begin_ordered_itemize"
                                )
                            }
                        )
                        opened_list = True
                    pass
                    local_indent_level = node["indent"]
                    indent_level = node["indent"]
                    if local_indent_level in list_type:
                        if not list_type[local_indent_level] == node["listStyleType"]:

                            new_data.append(
                                {
                                    "type": (
                                        "end_itemize"
                                        if list_type[local_indent_level] == "disc"
                                        else "end_ordered_itemize"
                                    )
                                }
                            )

                            new_data.append(
                                {
                                    "type": (
                                        "begin_itemize"
                                        if node["listStyleType"] == "disc"
                                        else "begin_ordered_itemize"
                                    )
                                }
                            )
                            pass
                    list_type[local_indent_level] = node["listStyleType"]
                    if indent_level > local_indent_level:
                        while not indent_level == local_indent_level:
                            new_data.append(
                                {
                                    "type": (
                                        "end_itemize"
                                        if list_type[indent_level] == "disc"
                                        else "end_ordered_itemize"
                                    )
                                }
                            )
                        indent_level -= 1
                    pass
                else:
                    if opened_list:
                        while not indent_level == 0:
                            new_data.append(
                                {
                                    "type": (
                                        "end_itemize"
                                        if list_type[indent_level] == "disc"
                                        else "end_ordered_itemize"
                                    )
                                }
                            )
                            indent_level -= 1
                        opened_list = False

                    pass
                pass
            else:
                if opened_list:
                    while not indent_level == 0:

                        new_data.append(
                            {
                                "type": (
                                    "end_itemize"
                                    if list_type[indent_level] == "disc"
                                    else "end_ordered_itemize"
                                )
                            }
                        )
                        indent_level -= 1
                    opened_list = False

                pass
            pass
        else:
            if opened_list:
                while not indent_level == 0:
                    new_data.append(
                        {
                            "type": (
                                "end_itemize"
                                if list_type[indent_level] == "disc"
                                else "end_ordered_itemize"
                            )
                        }
                    )
                    indent_level -= 1
                opened_list = False
            pass

        new_data.append(node)
    return new_data
