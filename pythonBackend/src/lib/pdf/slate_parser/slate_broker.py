import base64
import os
import pylatex.utils
from typing import List, Optional
from src.lib.pdf.slate_parser.parsers.get_simple_text_from_nodes import (
    get_simple_text_from_nodes,
)
from src.lib.pdf.slate_parser.parsers.parse_simple_text import parse_simple_text
from src.lib.pdf.slate_parser.parsers.parse_anonymous_text import parse_anonymous_text
from pylatex import (
    Document,
    Package,
    Center,
    FlushRight,
    FlushLeft,
    Command,
    NoEscape,
    Table,
    Tabular,
    Figure,
)
from pylatex.base_classes import Environment
from src.lib.pdf.slate_parser.slates_classes import (
    ListInformationTypeEnum,
    Slate_Image,
    Slate_Paragraph,
    Slate_Table,
    Slate_Table_TD,
    TextAlignEnum,
)
from pylatex.base_classes.command import Options
from ulid import ULID


class JUSTIFY(Environment):
    """A class to wrap LaTeX's alltt environment."""

    packages = [Package("ragged2e")]


def paragraph_parse(node: dict, doc: Document, tmpdirname: str):
    paragraph = Slate_Paragraph(**node)

    if not paragraph.indent == None:
        doc.append(Command("hspace", arguments=f"{str(paragraph.indent)}cm"))
    if not paragraph.lineHeight == None:
        doc.append(
            NoEscape(
                "\\setlength{\\baselineskip}{"
                + str(paragraph.lineHeight)
                + "\\baselineskip}"
            )
        )
    if not paragraph.listStyleType == None:
        if paragraph.listStyleType == ListInformationTypeEnum.disc:
            doc.append(NoEscape("\\hspace{0.5cm}\\textbullet"))
    if "children" in node:
        for child in list(node["children"]):
            slate_broker(node=child, doc=doc, tmpdirname=tmpdirname)


def generate_table_raws(columns: List[Slate_Table_TD], doc: Document):
    formatted_headers = list([])

    for column in columns:
        column_text = []
        get_simple_text_from_nodes(
            doc=doc, node=column.model_dump(), formatted_text=column_text
        )

        formatted_headers.append(
            NoEscape(
                r"\newline ".join(
                    map(
                        lambda x: x.dumps() if isinstance(x, Command) else x,
                        column_text,
                    )
                )
            )
        )

    return formatted_headers


def slate_broker(node: dict, doc: Document, tmpdirname: str) -> None:

    if not "type" in node:
        if not "children" in node:
            parse_simple_text(node=node, doc=doc)
        else:
            parse_anonymous_text(node=node, doc=doc)
            if "children" in node:
                for child in list(node["children"]):
                    slate_broker(node=child, doc=doc, tmpdirname=tmpdirname)
    else:
        match node["type"]:
            case "p" | "blockquote":
                paragraph = Slate_Paragraph(**node)

                if paragraph.align == TextAlignEnum.justify:
                    with doc.create(JUSTIFY()):
                        paragraph_parse(node=node, doc=doc, tmpdirname=tmpdirname)

                if paragraph.align == TextAlignEnum.center:
                    with doc.create(Center()):
                        paragraph_parse(node=node, doc=doc, tmpdirname=tmpdirname)

                if paragraph.align == TextAlignEnum.right:
                    with doc.create(FlushRight()):
                        paragraph_parse(node=node, doc=doc, tmpdirname=tmpdirname)

                if paragraph.align == TextAlignEnum.left:
                    with doc.create(FlushLeft()):
                        paragraph_parse(node=node, doc=doc, tmpdirname=tmpdirname)
                pass
            case "hr":
                doc.append(NoEscape(r"\par\noindent\rule{\textwidth}{0.5pt} "))
                pass
            case "page-break":
                doc.append(NoEscape(r"\clearpage"))
                pass
            case "table":
                slate_table = Slate_Table(**node)
                headers: List[Slate_Table_TD] = slate_table.children[0].children
                table_pec = " ".join(
                    list(map(lambda _x: f"p{{{1/len(headers)}\\linewidth}}", headers))
                )

                with doc.create(Table(position="h!")) as table:
                    table.append(NoEscape(r"\centering"))
                    with table.create(Tabular(table_pec)) as tabular:

                        tabular.add_hline()
                        for index, item in enumerate(slate_table.children):
                            if index == 0:
                                tabular.add_row(
                                    generate_table_raws(columns=item.children, doc=doc)
                                )  # En-têtes
                                tabular.add_hline()
                            else:
                                tabular.add_row(
                                    generate_table_raws(columns=item.children, doc=doc)
                                )  # En-têtes

                        tabular.add_hline()  # Ligne horizontale en bas
                pass
            case "img":
                img = Slate_Image(**node)
                img_data = base64.b64decode(img.url.split(",")[1])
                image_name = f"{ULID()}.png"
                tmp_image_path = os.path.join(tmpdirname, image_name)

                with open(tmp_image_path, "wb") as f:
                    f.write(img_data)
                with doc.create(Figure(position="h!")) as fig:
                    # Include the image in the LaTeX document
                    fig.add_image(
                        tmp_image_path,
                    )

                    if not img.caption == None:
                        caption_text = []
                        for child in img.caption:
                            get_simple_text_from_nodes(
                                node=child,
                                doc=doc,
                                formatted_text=caption_text,
                            )
                        fig.add_caption(
                            NoEscape(
                                r"\newline ".join(
                                    map(
                                        lambda x: (
                                            x.dumps() if isinstance(x, Command) else x
                                        ),
                                        caption_text,
                                    )
                                )
                            )
                        )
                    pass

            case _:
                pass
