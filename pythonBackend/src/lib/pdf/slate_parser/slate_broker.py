import base64
import os
from pprintpp import pprint
import pylatex.utils
from typing import List, Optional

import requests
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
    HorizontalSpace,
    MiniPage,
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
from dotenv import load_dotenv
from src.lib.pdf.slate_parser.parsers.create_kinetics_image import create_kinetic_image

load_dotenv()


class Quote(Environment):
    """Custom environment for the LaTeX 'quote'."""

    _latex_name = "quote"


class JUSTIFY(Environment):
    """A class to wrap LaTeX's alltt environment."""

    packages = [Package("ragged2e")]


def paragraph_parse(
    node: dict,
    doc: Document,
    tmpdirname: str,
    len_data: int,
    force_break: int,
    automatic_line_break: bool = True,
    floating_env: bool = True,
) -> bool:
    paragraph = Slate_Paragraph(**node)

    if not paragraph.lineHeight == None:
        doc.append(
            NoEscape(
                "\\setlength{\\baselineskip}{"
                + str(paragraph.lineHeight)
                + "\\baselineskip}"
            )
        )
    if node["listStyleType"] == "disc" or node["listStyleType"] == "decimal":
        doc.append(NoEscape(r"\item"))

    if "children" in node:
        for child in list(node["children"]):
            slate_broker(
                node=child,
                doc=doc,
                tmpdirname=tmpdirname,
                len_data=len_data,
                force_break=force_break,
                automatic_line_break=automatic_line_break,
                floating_env=floating_env,
            )


def generate_table_raws(
    columns: List[Slate_Table_TD],
    table: Document,
    tmpdirname: str,
    len_data: int,
    force_break: int,
    floating_env: bool = True,
):
    for column_index, column in enumerate(columns):
        for cell_index, cell in enumerate(column.children):
            slate_broker(
                node=cell,
                doc=table,
                tmpdirname=tmpdirname,
                len_data=len_data,
                force_break=force_break,
                automatic_line_break=False,
                floating_env=floating_env,
            )
            if cell_index < (len(column.children) - 1):
                table.append(NoEscape(r"\newline"))

            pass
        if column_index < (len(columns) - 1):
            table.append(NoEscape(r"&"))

        pass
    table.append(NoEscape(r"\\"))


def create_table(
    node: dict,
    doc: Document,
    tmpdirname: str,
    len_data: int,
    force_break: bool = False,
    floating_env: bool = True,
):
    slate_table = Slate_Table(**node)
    table_pec: str = ""
    headers: List[Slate_Table_TD] = slate_table.children[0].children

    if "colSizes" in node:
        undefined_size = node["colSizes"].count(0)
        total_defined_length = sum(node["colSizes"])
        remaining_length = total_len - total_defined_length
        if remaining_length < 0:
            remaining_length = 0

        table_pec = " ".join(
            list(
                map(
                    lambda x: f"p{{{0.9 * (x if not x == 0 else remaining_length/undefined_size)/total_len}\\linewidth}}",
                    node["colSizes"],
                )
            )
        )
        pass
    else:
        table_pec = " ".join(
            list(
                map(
                    lambda _x: f"p{{{0.9/len(headers)}\\linewidth}}",
                    headers,
                )
            )
        )
        pass
    doc.append(NoEscape(r"\centering"))
    doc.append(NoEscape(r"\resizebox{0.9\linewidth}{!}{"))
    with doc.create(Tabular(table_pec)) as tabular:

        tabular.add_hline()
        for row_index, row in enumerate(slate_table.children):

            if row_index == 0:
                generate_table_raws(
                    columns=row.children,
                    table=doc,
                    tmpdirname=tmpdirname,
                    len_data=len_data,
                    floating_env=floating_env,
                    force_break=force_break,
                )
                tabular.add_hline()
            else:
                generate_table_raws(
                    columns=row.children,
                    table=doc,
                    tmpdirname=tmpdirname,
                    len_data=len_data,
                    floating_env=floating_env,
                    force_break=force_break,
                )
                pass

        tabular.add_hline()  # Ligne horizontale en bas
    doc.append(NoEscape("}"))
    pass


total_len = 670


def slate_broker(
    node: dict,
    doc: Document,
    tmpdirname: str,
    len_data: int,
    automatic_line_break: bool = True,
    floating_env: bool = True,
    force_break: bool = False,
):
    # pprint(node, depth=4)
    if not "type" in node:

        if not "children" in node:
            parse_simple_text(node=node, doc=doc)
        else:
            parse_anonymous_text(node=node, doc=doc)
            if "children" in node:
                for child in list(node["children"]):
                    slate_broker(
                        node=child,
                        doc=doc,
                        tmpdirname=tmpdirname,
                        len_data=len_data,
                        force_break=force_break,
                        automatic_line_break=automatic_line_break,
                        floating_env=floating_env,
                    )

    else:
        match node["type"]:
            case "p" | "toggle":
                if (
                    not node["type"] == "p"
                    or not "listStyleType" in node
                    or not "indent" in node
                ):
                    node["type"] = "p"
                    node["listStyleType"] = None
                    node["indent"] = None
                    pass
                paragraph = Slate_Paragraph(**node)
                # pprint(node, depth=4)

                if (
                    node["listStyleType"] == "disc"
                    or node["listStyleType"] == "decimal"
                ):
                    paragraph_parse(
                        node=node,
                        doc=doc,
                        tmpdirname=tmpdirname,
                        len_data=len_data,
                        force_break=force_break,
                        automatic_line_break=automatic_line_break,
                        floating_env=floating_env,
                    )
                else:

                    if "align" in paragraph:

                        if paragraph.align == TextAlignEnum.justify:
                            with doc.create(JUSTIFY()):
                                paragraph_parse(
                                    node=node,
                                    doc=doc,
                                    tmpdirname=tmpdirname,
                                    len_data=len_data,
                                    force_break=force_break,
                                    automatic_line_break=automatic_line_break,
                                    floating_env=floating_env,
                                )

                        if paragraph.align == TextAlignEnum.center:
                            with doc.create(Center()):
                                paragraph_parse(
                                    node=node,
                                    doc=doc,
                                    tmpdirname=tmpdirname,
                                    len_data=len_data,
                                    force_break=force_break,
                                    automatic_line_break=automatic_line_break,
                                    floating_env=floating_env,
                                )

                        if paragraph.align == TextAlignEnum.right:
                            with doc.create(FlushRight()):
                                paragraph_parse(
                                    node=node,
                                    doc=doc,
                                    tmpdirname=tmpdirname,
                                    len_data=len_data,
                                    force_break=force_break,
                                    automatic_line_break=automatic_line_break,
                                    floating_env=floating_env,
                                )

                        if paragraph.align == TextAlignEnum.left:
                            with doc.create(FlushLeft()):
                                paragraph_parse(
                                    node=node,
                                    doc=doc,
                                    tmpdirname=tmpdirname,
                                    len_data=len_data,
                                    force_break=force_break,
                                    automatic_line_break=automatic_line_break,
                                    floating_env=floating_env,
                                )
                    else:
                        # with doc.create(FlushLeft()):
                        if not paragraph.indent == None:
                            doc.append(HorizontalSpace(f"{paragraph.indent/2}cm"))
                        paragraph_parse(
                            node=node,
                            doc=doc,
                            tmpdirname=tmpdirname,
                            len_data=len_data,
                            force_break=force_break,
                            automatic_line_break=automatic_line_break,
                            floating_env=floating_env,
                        )
                        pass
                    if automatic_line_break:
                        if "text" in paragraph.children[0]:
                            if paragraph.children[0]["text"] == "":
                                doc.append(NoEscape(r"\vspace*{\baselineskip}"))
                            else:

                                doc.append(NoEscape(r"\\"))
                                pass
                        else:
                            # pprint(node, depth=4)
                            if force_break:
                                doc.append(NoEscape(r"\\"))
                            pass
                    data_input_container = False
                    for el in node["children"]:
                        if "type" in el:
                            if el["type"] == "data-input":
                                data_input_container = True
                    if data_input_container:
                        doc.append(NoEscape(r"\\"))

                pass
            case "blockquote":
                with doc.create(Quote()) as quote:
                    doc.append(NoEscape(r"``"))
                    for child in node["children"]:
                        slate_broker(
                            doc=quote,
                            node=child,
                            tmpdirname=tmpdirname,
                            len_data=len_data,
                            automatic_line_break=automatic_line_break,
                            force_break=force_break,
                            floating_env=floating_env,
                        )
                    doc.append(NoEscape(r"''"))

                pass
            case "hr":
                doc.append(NoEscape(r"\par\noindent\rule{\textwidth}{0.5pt} "))
                pass
            case "page-break":
                doc.append(NoEscape(r"\clearpage"))
                pass
            case "h1":

                doc.append(Command("LARGE"))
                for child in list(node["children"]):
                    child["bold"] = True
                    slate_broker(
                        node=child,
                        doc=doc,
                        tmpdirname=tmpdirname,
                        len_data=len_data,
                        automatic_line_break=automatic_line_break,
                        force_break=force_break,
                        floating_env=floating_env,
                    )
                if automatic_line_break:
                    doc.append(NoEscape(r"\\ \normalsize"))
                else:
                    doc.append(NoEscape(r"\normalsize"))
                pass
            case "h2":

                doc.append(Command("Large"))
                for child in list(node["children"]):
                    child["bold"] = True
                    slate_broker(
                        node=child,
                        doc=doc,
                        tmpdirname=tmpdirname,
                        len_data=len_data,
                        automatic_line_break=automatic_line_break,
                        force_break=force_break,
                        floating_env=floating_env,
                    )
                if automatic_line_break:
                    doc.append(NoEscape(r"\\ \normalsize"))
                else:
                    doc.append(NoEscape(r"\normalsize"))

                pass
            case "h3":

                doc.append(Command("large"))
                for child in list(node["children"]):
                    child["bold"] = True
                    slate_broker(
                        node=child,
                        doc=doc,
                        tmpdirname=tmpdirname,
                        len_data=len_data,
                        automatic_line_break=automatic_line_break,
                        force_break=force_break,
                        floating_env=floating_env,
                    )
                if automatic_line_break:
                    doc.append(NoEscape(r"\\ \normalsize"))
                else:
                    doc.append(NoEscape(r"\normalsize"))

                pass
            case "table":
                if floating_env:
                    with doc.create(Table(position="h!")) as table:
                        create_table(
                            doc=table,
                            floating_env=floating_env,
                            node=node,
                            len_data=len_data,
                            tmpdirname=tmpdirname,
                        )
                else:
                    create_table(
                        doc=doc,
                        floating_env=floating_env,
                        node=node,
                        len_data=len_data,
                        tmpdirname=tmpdirname,
                    )
                pass
            case "img":
                img = Slate_Image(**node)
                # pprint(node, depth=4)
                tmp_image_path = None
                if img.url.startswith("data"):
                    img_data = base64.b64decode(img.url.split(",")[1])
                    image_name = f"{ULID()}.png"
                    tmp_image_path = os.path.join(tmpdirname, image_name)

                    with open(tmp_image_path, "wb") as f:
                        f.write(img_data)
                if img.url.startswith("http"):
                    response = requests.get(
                        img.url.replace(
                            "app.bolt.local/app-storage",
                            f"{os.getenv('STORAGE_HOST')}:9000/uploads",
                        )
                    )
                    extension = img.url.split(".")[-1]
                    # print(response.status_code)
                    if response.status_code == 200:
                        image_name = f"{ULID()}.{extension}"
                        tmp_image_path = os.path.join(tmpdirname, image_name)

                        with open(tmp_image_path, "wb") as f:
                            f.write(response.content)

                if not tmp_image_path == None:
                    width = 1
                    if "width" in node:
                        width = node["width"] / total_len
                    if floating_env:
                        with doc.create(Figure(position="h!")) as fig:
                            # Include the image in the LaTeX document
                            fig.add_image(
                                tmp_image_path, width=NoEscape(f"{width}\\textwidth")
                            )
                            fig.append(NoEscape(r"\caption{"))
                            if not img.caption == None:
                                for child in img.caption:
                                    slate_broker(
                                        node=child,
                                        doc=fig,
                                        tmpdirname=tmpdirname,
                                        len_data=len_data,
                                        automatic_line_break=False,
                                        force_break=force_break,
                                        floating_env=floating_env,
                                    )
                            fig.append(NoEscape(r"}"))
                    else:
                        doc.append(NoEscape(r"\centering"))
                        doc.append(
                            NoEscape(
                                f"\\includegraphics[width=0.9\\textwidth]{{ {tmp_image_path} }}"
                            )
                        )

                pass
            case "begin_itemize":
                doc.append(NoEscape(r"\begin{itemize}"))
                pass
            case "end_itemize":
                doc.append(NoEscape(r"\end{itemize}"))
                pass
            case "begin_ordered_itemize":
                doc.append(NoEscape(r"\begin{enumerate}"))
                pass
            case "end_ordered_itemize":
                doc.append(NoEscape(r"\end{enumerate}"))
                pass
            case "column_group":

                if "layout" in node:

                    for index, fraction in enumerate(node["layout"]):
                        with doc.create(
                            MiniPage(width=NoEscape(f"{fraction/100}\\linewidth"))
                        ) as column:
                            for child in node["children"][index]["children"]:
                                slate_broker(
                                    node=child,
                                    doc=column,
                                    tmpdirname=tmpdirname,
                                    len_data=len_data,
                                    automatic_line_break=automatic_line_break,
                                    force_break=force_break,
                                    floating_env=False,
                                )
                    doc.append(
                        NoEscape(r"\hspace{\textwidth}")
                    )  # Optional spacing between columns
                pass
            case "display-kinetic":
                doc.append(NoEscape(r"\\"))

                display_count = 0

                if node["HypoKinetic"]["show"]:
                    display_count += 1
                if node["AKinetic"]["show"]:
                    display_count += 1
                if node["Dyskinetic"]["show"]:
                    display_count += 1

                if display_count > 0:
                    if node["HypoKinetic"]["show"]:
                        create_kinetic_image(
                            doc=doc,
                            kinetics_type="Hypokinesie",
                            color="hypokinetic_color",
                            config=node["HypoKinetic"]["kinetic"],
                            display_count=display_count,
                        )
                    if node["AKinetic"]["show"]:
                        create_kinetic_image(
                            doc=doc,
                            kinetics_type="Akinésie",
                            color="akinetic_color",
                            config=node["AKinetic"]["kinetic"],
                            display_count=display_count,
                        )
                    if node["Dyskinetic"]["show"]:
                        create_kinetic_image(
                            doc=doc,
                            kinetics_type="Dyskinésie",
                            color="dyskinetic_color",
                            config=node["Dyskinetic"]["kinetic"],
                            display_count=display_count,
                        )
                if len_data > 1:
                    doc.append(NoEscape(r"\\"))
                pass
            case "data-input":
                # pprint(node, depth=4)
                match node["inputType"]:
                    case "number" | "text" | "select" | "date":
                        doc.append(node["value"])
                        pass
                    case "checkbox":
                        doc.append(
                            f"{"présence de " if node['value'] else 'absence de '} {node["label"]}"
                        )
                        pass
                    case "multiple":
                        doc.append(
                            ", ".join(map(lambda x: x["value"], node["multiValues"]))
                        )
                        pass
                    case _:
                        pass
                pass
            case _:
                # pprint(node, depth=4)
                # doc.append(NoEscape(r"non pris en charge"))

                pass
