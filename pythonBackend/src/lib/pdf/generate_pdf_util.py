import os
from typing import List, Optional
from pprintpp import pprint
from pylatex import Command, Document, MiniPage, Center
from pylatex.utils import NoEscape
from pylatex.base_classes.command import Options
from src.lib.pdf.slate_parser.slate_broker import slate_broker
from src.lib.pdf.slate_parser.slates_classes import (
    PageSizeEnum,
    Patient,
    PDF_settings,
    QueryParams,
)
from datetime import datetime

cwd = os.getcwd()


def generate_pdf(
    tmpdirname: str,
    data: List[dict],
    settings: PDF_settings,
    query_params: QueryParams,
    documentTitle: str,
    patient: Optional[Patient] = None,
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
    doc.packages.append(NoEscape(r"\usepackage[HTML]{xcolor}"))
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
    doc.preamble.append(Command("usepackage", "array"))
    doc.packages.append(NoEscape(r"\usepackage{ifthen}"))
    doc.preamble.append(Command("usepackage", NoEscape("eso-pic")))
    doc.packages.append(NoEscape(r"\usepackage{fancyhdr}"))
    doc.packages.append(NoEscape(r"\usepackage{tikz}"))
    doc.packages.append(NoEscape(r"\usepackage{unicode-math}"))
    doc.packages.append(NoEscape(r"\usepackage{fontspec}"))
    doc.preamble.append(Command("usepackage", "tcolorbox"))
    doc.preamble.append(Command("usepackage", "inputenc"))
    doc.preamble.append(Command("usepackage", "enumitem"))

    doc.preamble.append(NoEscape(r"\setlist{topsep=0pt} "))

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

    doc.preamble.append(NoEscape(r"\renewcommand{\arraystretch}{1.5}"))

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
    # define colors
    doc.preamble.append(
        NoEscape(r"\definecolor{main_title_background_color}{HTML}{e2e8f0}")
    )
    doc.preamble.append(
        NoEscape(r"\definecolor{main_title_border_color}{HTML}{1e293b}")
    )
    doc.preamble.append(NoEscape(r"\definecolor{kinetic_base_color}{HTML}{f1f5f9}"))
    doc.preamble.append(NoEscape(r"\definecolor{hypokinetic_color}{HTML}{fecdd3}"))
    doc.preamble.append(NoEscape(r"\definecolor{akinetic_color}{HTML}{f87171}"))
    doc.preamble.append(NoEscape(r"\definecolor{dyskinetic_color}{HTML}{fcd34d}"))

    if not patient == None:
        # Get today's date
        today = datetime.today()

        # Format today's date
        formatted_date = today.strftime("%d/%m/%Y")
        with doc.create(MiniPage(width=NoEscape(f"{0.5}\\linewidth"))) as column:
            column.append(
                NoEscape(
                    f"\\textbf{{\\underline{{Nom :}}}} \\hspace{{1cm}} {patient.last_name}"
                )
            )
            column.append(NoEscape(r"\\"))
            column.append(
                NoEscape(
                    f"\\textbf{{\\underline{{Prénom :}}}} \\hspace{{1cm}} {patient.first_name}"
                )
            )
            column.append(NoEscape(r"\\"))

        with doc.create(MiniPage(width=NoEscape(f"{0.5}\\linewidth"))) as column:
            column.append(
                NoEscape(
                    f"\\textbf{{\\underline{{DDN :}}}} \\hspace{{1cm}} {patient.dob}"
                )
            )
            column.append(NoEscape(r"\\"))
            column.append(
                NoEscape(
                    f"\\textbf{{\\underline{{Date :}}}} \\hspace{{1cm}} {formatted_date}"
                )
            )
            column.append(NoEscape(r"\\"))
        doc.append(NoEscape(r"\hspace{\textwidth}"))  # Optional spacing between columns
        doc.append(NoEscape(r"\\"))
    with doc.create(Center()):
        doc.append(
            NoEscape(
                f"""
        \\begin{{tcolorbox}}[
            colframe=main_title_border_color,        % Couleur de la bordure
            colback=main_title_background_color,        % Couleur de fond
            coltitle=main_title_border_color,       % Couleur du texte (si titre utilisé)
            arc=8pt,              % Rayon des coins arrondis
            boxrule=0.5mm,          % Épaisseur de la bordure
            auto outer arc,       % Ajuste automatiquement les coins arrondis
            width=\\linewidth,     % Largeur de la boîte
            halign=center         % Centrer le texte horizontalement
        ]
        \\LARGE{{\\textbf{{{documentTitle}}}}}
        \\end{{tcolorbox}}
        """
            )
        )

    # pprint(data, depth=4)

    if len(data) == 0:
        doc.append("No data")
    else:
        for node_index, node in enumerate(data):
            slate_broker(
                data=data,
                node_index=node_index,
                node=node,
                doc=doc,
                tmpdirname=tmpdirname,
                len_data=len(data),
            )

    pdf_file_path = os.path.join(tmpdirname, pdf_name)
    doc.generate_pdf(clean_tex=False, filepath=pdf_file_path, compiler="lualatex")
    # doc.generate_pdf(clean_tex=False)

    return f"{pdf_file_path}.pdf"


if __name__ == "__main__":
    generate_pdf()
