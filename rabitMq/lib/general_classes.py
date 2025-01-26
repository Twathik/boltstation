# Define Enum for sexe
from typing import Awaitable, Callable, List
from pydantic import BaseModel
from pyparsing import Enum
from ulid import ULID


AsyncVoidFunction = Callable[[], Awaitable[None]]
