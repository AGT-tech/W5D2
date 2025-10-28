from typing import Protocol, Optional
from src.domain.order import Order, OrderItem

class OrderRepository(Protocol):
  def sace(self, order:Order) -> Optional[Order]: ...
    sef find_by_id(self
