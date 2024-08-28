from dataclasses import dataclass

@dataclass
class FilterCriteria:
    marka_name: str = None
    year_from: int = None
    year_to: int = None
    price_from: float = None
    price_to: float = None


@dataclass
class Mark:
    MARKA_ID: str
    MARKA_NAME: str
