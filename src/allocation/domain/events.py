# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from datetime import date
from typing import Optional

class Event:
    pass

@dataclass
class Allocated(Event):
    orderid: str
    sku: str
    qty: int
    batchref: str

@dataclass
class OutOfStock(Event):
    sku: str
