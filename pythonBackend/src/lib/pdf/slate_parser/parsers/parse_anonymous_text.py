from pprintpp import pprint
from pylatex import Document

from src.lib.pdf.slate_parser.slates_classes import Slate_AnonymousText


def parse_anonymous_text(node: dict, doc: Document):
    pprint(node)
    anonymousText = Slate_AnonymousText(**node)
