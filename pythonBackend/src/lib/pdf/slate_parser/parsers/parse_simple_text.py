from os import replace
from typing import Optional
from click import argument
from pprintpp import pprint
from pylatex import Document, Command
from pylatex.base_classes.command import Options
from src.lib.pdf.slate_parser.slates_classes import Slate_SimpleText
from src.lib.pdf.slate_parser.parsers.convert_rgb_to_hex import rgb_to_hex_if_rgb


def parse_simple_text(node: dict, doc: Document, append: Optional[bool] = True) -> bool:

    simpleText = Slate_SimpleText(**node)

    formattedText = simpleText.text

    formattedText = (
        Command("sout", formattedText) if simpleText.strikethrough else formattedText
    )
    formattedText = (
        Command("ul", formattedText) if simpleText.underline else formattedText
    )
    formattedText = (
        Command("textit", formattedText) if simpleText.italic else formattedText
    )
    formattedText = (
        Command("textbf", formattedText) if simpleText.bold else formattedText
    )

    formattedText = (
        Command("textsuperscript", formattedText)
        if simpleText.superscript
        else formattedText
    )
    formattedText = (
        Command("textsubscript", formattedText)
        if simpleText.subscript
        else formattedText
    )
    formattedText = (
        Command(
            "textcolor",
            options=Options(["HTML"]),
            arguments=[
                rgb_to_hex_if_rgb(simpleText.color).replace("#", ""),
                formattedText,
            ],
        )
        if not simpleText.color == None
        else formattedText
    )
    # TODO fix the no wraping issue
    formattedText = (
        Command(
            "colorbox",
            options=Options(["HTML"]),
            arguments=[simpleText.backgroundColor.replace("#", ""), formattedText],
        )
        if not simpleText.backgroundColor == None
        else formattedText
    )
    if append == True:
        doc.append(formattedText)
        return
    return formattedText
