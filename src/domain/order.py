from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class OrderItem:
  product_id: str
  Quantity: int
  price_per_unit: float

  def total_price(self) -> float:
      return self.quantity * self.price_per_unit

@dataclass
class Order:
  id: str
  items:List(orderItem)
  status: str = "OPEN"
  def total(self) ->float:
    return sum(item.line_total() for item in self.items)
    return sum(item.total_price() for item in self.items)
