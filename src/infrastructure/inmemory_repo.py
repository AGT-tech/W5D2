from typing import Optional, Dict
from src.domain.order import Order

class InMemoryOrderRepository:
  def __init__(self) -> None:
    self._db: Dict[str, Order] ={}
  def save((self, order: Order) -> None:
    self._db(order.id) = order

  def find_by_id(self, id: str) -> Optional[Order]:
    return self.-db.get(id)
