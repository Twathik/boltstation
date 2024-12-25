from __future__ import annotations
from enum import Enum
from typing import Any, List, Literal, Optional, Union
from pydantic import BaseModel, ConfigDict


# Define an Enum
class TextAlignEnum(str, Enum):
    justify = "justify"
    right = "right"
    center = "center"
    left = "left"


class ListInformationTypeEnum(str, Enum):
    disc = "disc"
    decimal = "decimal"


class InputTypeEnum(str, Enum):
    text = "text"
    select = "select"
    number = "number"
    date = "date"
    multiple = "multiple"
    checkbox = "checkbox"


class EventTypesEnum(str, Enum):
    BIOLOGY = "BIOLOGY"
    CERTIFICAT = "CERTIFICAT"
    CLINICALEXAM = "CLINICALEXAM"
    DIAGNOSTIC = "DIAGNOSTIC"
    ECG = "ECG"
    EXTERNAL_DOCUMENT = "EXTERNAL_DOCUMENT"
    HISTORY = "HISTORY"
    HOSPITALIZATION = "HOSPITALIZATION"
    MEDICAL_REPORT = "MEDICAL_REPORT"
    PRESCRIPTION = "PRESCRIPTION"
    SONOGRAPHY = "SONOGRAPHY"


class PageSizeEnum(str, Enum):
    A4 = "A4"
    A5 = "A5"


# Define models
class Slate_SimpleText(BaseModel):
    text: str
    id: Optional[str] = None
    type: Optional[str] = None

    createdAt: Optional[str] = None
    bold: Optional[bool] = False
    italic: Optional[bool] = False
    strikethrough: Optional[bool] = False
    underline: Optional[bool] = False
    superscript: Optional[bool] = False
    subscript: Optional[bool] = False
    color: Optional[str] = None  # Fixed default value
    backgroundColor: Optional[str] = None  # Fixed default value


class Slate_AnonymousText(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    children: Optional[List[Any]] = None  # Fixed forward reference as string
    createdAt: Optional[str] = None


class Slate_Paragraph(BaseModel):
    id: Optional[str] = None
    type: Literal["p"]
    children: List[Any]
    align: Optional[TextAlignEnum] = None
    createdAt: Optional[str] = None
    indent: Optional[int] = None
    lineHeight: Optional[int] = None
    listStyleType: Optional[ListInformationTypeEnum] = None
    listStart: Optional[int] = None


class Slate_HorizontalRule(BaseModel):
    id: Optional[str] = None
    type: Literal["hr"]
    children: List[Any]
    createdAt: Optional[str] = None


class Slate_PageBreak(BaseModel):
    id: Optional[str] = None
    type: Literal["page-break"]
    children: List[Any]
    createdAt: Optional[str] = None


class Slate_Blockquote(BaseModel):
    id: Optional[str] = None
    type: Literal["blockquote"]
    children: List[Any]
    createdAt: Optional[str] = None


class Slate_Table_TD(BaseModel):
    id: Optional[str] = None
    type: Literal["td"]
    children: List[Any]


class Slate_Table_TR(BaseModel):
    id: Optional[str] = None
    type: Literal["tr"]
    children: List[Slate_Table_TD]


class Slate_Table(BaseModel):
    id: Optional[str] = None
    type: Literal["table"]
    children: List[Slate_Table_TR]
    width: Optional[int] = None
    caption: Optional[List[Slate_SimpleText]] = None
    createdAt: Optional[str] = None


class Slate_Image(BaseModel):
    id: Optional[str] = None
    type: Literal["img"]
    children: List[Any]
    url: str
    createdAt: Optional[str] = None
    caption: Optional[Any] = None


class Slate_Column_Element(BaseModel):
    id: Optional[str] = None
    type: Literal["column-element"]
    children: List[Any]
    columnTemplate: str
    createdAt: Optional[str] = None


class Slate_Column_Container(BaseModel):
    id: Optional[str] = None
    type: Literal["column-container"]
    children: List[Slate_Column_Element]
    createdAt: Optional[str] = None


class Slate_DataInput(BaseModel):
    id: Optional[str] = None
    type: Literal["data-input"]
    children: List[Any]
    createdAt: Optional[str] = None
    inputType: InputTypeEnum
    value: Union[int, str, List[str]]


class Slate_KineticInput(BaseModel):
    id: Optional[str] = None
    type: Literal["Kinetic-input"]
    children: List[Any]
    createdAt: Optional[str] = None


class Slate_Kinetic17state(BaseModel):
    sgt1: bool
    sgt2: bool
    sgt3: bool
    sgt4: bool
    sgt5: bool
    sgt6: bool
    sgt7: bool
    sgt8: bool
    sgt9: bool
    sgt10: bool
    sgt11: bool
    sgt12: bool
    sgt13: bool
    sgt14: bool
    sgt15: bool
    sgt16: bool
    sgt17: bool


class Slate_SingleKineticType(BaseModel):
    show: bool
    kinetic: Slate_Kinetic17state


class Slate_DisplayKineticElementType(BaseModel):
    id: Optional[str] = None
    type: Literal["display-kinetic"]
    children: List[Any]
    HypoKinetic: Slate_SingleKineticType
    AKinetic: Slate_SingleKineticType
    Dyskinetic: Slate_SingleKineticType
    modifiedAt: Optional[str] = None
    documentType: EventTypesEnum
    className: Optional[str]


class PDF_paddings(BaseModel):
    A4paddingTop: int
    A4paddingBottom: int
    A4paddingLeft: int
    A4paddingRight: int
    A5paddingTop: int
    A5paddingBottom: int
    A5paddingLeft: int
    A5paddingRight: int
    model_config = ConfigDict(frozen=False)


class PDF_Urls(BaseModel):
    oddUrl: str
    evenUrl: str
    model_config = ConfigDict(frozen=False)


class PDF_settings(BaseModel):
    paddings: PDF_paddings
    urls: PDF_Urls
    model_config = ConfigDict(frozen=False)


class QueryParams(BaseModel):
    page_size: Optional[PageSizeEnum] = None
