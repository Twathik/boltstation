from typing import List

from pprintpp import pprint


def format_lists(data: List[dict]) -> List[dict]:
    formatted_data: List[dict] = []
    new_data: List[dict] = []
    indent_level = 0
    list_type: dict = {}
    for node in data:
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
                                    {**child, "strikethrough": True, "color": "#475569"}
                                )
                            node["children"] = children
                            pass
        formatted_data.append(node)
    formatted_data.append(
        {"type": "p", "indent": None, "listStyleType": None, "children": [{"text": ""}]}
    )

    for node in formatted_data:
        if "type" in node:
            if node["type"] == "p":
                if not node["indent"] == None and (
                    node["listStyleType"] == "disc"
                    or node["listStyleType"] == "decimal"
                ):

                    local_indent_level = node["indent"]
                    # print("indent", node["indent"], "local", local_indent_level)
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
                    pass
                else:
                    local_indent_level = 0
                    # print("-----no indent-----", indent_level)
                    pass
                pprint(list_type, depth=4)
                if indent_level < local_indent_level:
                    new_data.append(
                        {
                            "type": (
                                "begin_itemize"
                                if list_type[local_indent_level] == "disc"
                                else "begin_ordered_itemize"
                            )
                        }
                    )
                    indent_level = local_indent_level
                    pass

                if indent_level > local_indent_level:
                    while indent_level > local_indent_level:
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

                    pass

        new_data.append(node)
        pass

    return new_data