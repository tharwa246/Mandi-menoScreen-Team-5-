from dataclasses import dataclass

@dataclass
class ScreeningQuestion:
    id: int
    text: str
    type: str
    category: str
    options: list