from typing import List
from src.domain.order import Order, OrderItem
from src.application.ports import OrderRepository

class OrderService:
  def __init__(self, repository: OrderRepository):
    self.repository p= repository
  def create_order(self
