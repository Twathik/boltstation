from pylatex import Document

from src.lib.pdf.slate_parser.parsers.parse_simple_text import parse_simple_text


def get_simple_text_from_nodes(node: dict, doc: Document, formatted_text=[]):

    if not "children" in node:
        formatted_text.append(parse_simple_text(node=node, doc=doc, append=False))
    else:
        if "children" in node:
            for child in list(node["children"]):
                get_simple_text_from_nodes(
                    node=child, doc=doc, formatted_text=formatted_text
                )
