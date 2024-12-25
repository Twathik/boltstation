import os
from typing import Optional
from pylatex import Command, Document
from pylatex.utils import NoEscape
from pylatex.base_classes.command import Options
from src.lib.pdf.slate_parser.slate_broker import slate_broker
from src.lib.pdf.slate_parser.slates_classes import (
    PDF_settings,
    PageSizeEnum,
    QueryParams,
)

cwd = os.getcwd()


def generate_pdf(
    tmpdirname: str, data: dict, settings: PDF_settings, query_params: QueryParams
):
    # Basic document

    pdf_name = "document"
    doc = Document(pdf_name)
    page_format = "a5paper" if query_params.page_size == PageSizeEnum.A5 else "a4paper"
    doc.documentclass = Command(
        "documentclass",
        options=Options("12pt", page_format),
        arguments="article",
    )

    doc.packages.append(NoEscape(r"\usepackage{ulem}"))
    doc.packages.append(NoEscape(r"\usepackage{xcolor}"))
    doc.packages.append(NoEscape(r"\usepackage{soul}"))
    doc.preamble.append(Command("usepackage", "geometry"))
    if query_params.page_size == PageSizeEnum.A5:
        doc.preamble.append(
            NoEscape(
                f"\\geometry{{top={settings.paddings.A5paddingTop}mm, bottom={settings.paddings.A5paddingBottom}mm, outer={settings.paddings.A5paddingRight}mm, inner={settings.paddings.A5paddingLeft}mm}}"
            )
        )
    else:
        doc.preamble.append(
            NoEscape(
                f"\\geometry{{top={settings.paddings.A4paddingTop}mm, bottom={settings.paddings.A4paddingBottom}mm, outer={settings.paddings.A4paddingRight}mm, inner={settings.paddings.A4paddingLeft}mm}}"
            )
        )
    doc.preamble.append(Command("usepackage", "graphicx"))
    doc.packages.append(NoEscape(r"\usepackage{ifthen}"))
    doc.preamble.append(Command("usepackage", NoEscape("eso-pic")))
    doc.packages.append(NoEscape(r"\usepackage{fancyhdr}"))
    doc.packages.append(NoEscape(r"\usepackage{tikz}"))

    doc.preamble.append(
        NoEscape(
            r"""
            \pagestyle{fancy}
            \fancyhf{} % Clear existing headers and footers
            \fancyhead{} % Clear the header
            \fancyfoot[C]{% Centered footer
                \mbox{\tikz[baseline=(page.base)]{
                    \node[draw=black, fill=white, rounded corners=3pt, inner sep=3pt] (page) {\thepage};
                }}
            }
            \renewcommand{\headrulewidth}{0pt} % Remove the top black line
            \renewcommand{\footrulewidth}{0pt} % Remove any footer line
            """
        )
    )

    # Define commands for odd and even backgrounds
    doc.preamble.append(
        NoEscape(
            r"""
    \newcommand\OddBackgroundPic{
        \put(0,0){%
            \parbox[b][\paperheight]{\paperwidth}{%
                \vfill
                \centering
                \includegraphics[width=\paperwidth,height=\paperheight]{"""
            + settings.urls.evenUrl
            + r"""}
                \vfill
            }
        }
    }
    """
        )
    )

    doc.preamble.append(
        NoEscape(
            r"""
    \newcommand\EvenBackgroundPic{
        \put(0,0){%
            \parbox[b][\paperheight]{\paperwidth}{%
                \vfill
                \centering
                \includegraphics[width=\paperwidth,height=\paperheight]{"""
            + settings.urls.oddUrl
            + r"""}
                \vfill
            }
        }
    }
    """
        )
    )

    # Add conditional background logic
    doc.preamble.append(
        NoEscape(
            r"""
    \AddToShipoutPictureBG{%
        \ifthenelse{\isodd{\value{page}}}{\OddBackgroundPic}{\EvenBackgroundPic}%
    }
    """
        )
    )
    if len(data) == 0:
        doc.append("No data")
    else:
        for node in data:
            slate_broker(node=node, doc=doc, tmpdirname=tmpdirname)
    pdf_file_path = os.path.join(tmpdirname, pdf_name)
    doc.generate_pdf(clean_tex=False, filepath=pdf_file_path)
    doc.generate_pdf(clean_tex=False)

    return f"{pdf_file_path}.pdf"


if __name__ == "__main__":
    generate_pdf()
