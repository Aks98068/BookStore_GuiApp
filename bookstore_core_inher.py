"""
Book Ordering System - Core Classes with Inheritance
This module contains the core classes for the book ordering system with inheritance structure.
"""

from datetime import datetime
from typing import Optional, List

class Person:
    """Base class for persons in the system."""
    def __init__(self, name: str, phone: str, email: str):
        self._name = name
        self._phone = phone
        self._email = email

    @property
    def name(self) -> str:
        """Get person's name."""
        return self._name

    @property
    def phone(self) -> str:
        """Get person's phone number."""
        return self._phone

    @property
    def email(self) -> str:
        """Get person's email."""
        return self._email

class Customer(Person):
    """Customer class inheriting from Person."""
    def __init__(self, name: str, phone: str, email: str):
        super().__init__(name, phone, email)

class Product:
    """Base class for products in the system."""
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        """Get product name."""
        return self._name

    @property
    def price(self) -> float:
        """Get product price."""
        return self._price

class Stock(Product):
    """Stock class inheriting from Product."""
    def __init__(self, book_name: str, author: str, price: float):
        super().__init__(book_name, price)
        self._author = author

    @property
    def author(self) -> str:
        """Get book author."""
        return self._author

    @property
    def book_name(self) -> str:
        """Get book name."""
        return self.name

class Order:
    """Class representing an order in the system."""
    def __init__(self, customer: Customer, stock: Stock):
        self.customer = customer
        self.stock = stock

class Shipping:
    """Class handling shipping details and calculations."""
    URGENT_COST = 5.45
    STANDARD_COST = 3.95

    def __init__(self, order: Order, ship_date: datetime):
        self.order = order
        self.ship_date = ship_date
        self._ship_cost = 0.0
        self.count_urgent = 0

    def set_ship_cost(self, is_urgent: bool = False) -> None:
        """Set shipping cost based on urgency."""
        if is_urgent:
            self._ship_cost = self.URGENT_COST
            self.count_urgent += 1
        else:
            self._ship_cost = self.STANDARD_COST

    def calc_ship_cost(self) -> float:
        """Calculate and return shipping cost."""
        return self._ship_cost

class Invoice:
    """Class handling invoice generation and calculations."""
    def __init__(self, invoice_nbr: str, stock: Stock, ship_order: Shipping):
        self.invoice_nbr = invoice_nbr
        self.stock = stock
        self.ship_order = ship_order
        self.total_cost = 0.0

    def calculate_total(self) -> float:
        """Calculate total cost including book price and shipping."""
        self.total_cost = self.stock.price + self.ship_order.calc_ship_cost()
        return self.total_cost

class BookStore:
    """Class managing the bookstore operations and invoice repository."""
    def __init__(self):
        self.invoices: List[Invoice] = []

    def add_invoice(self, invoice: Invoice) -> None:
        """Add an invoice to the repository."""
        self.invoices.append(invoice)

    def search_invoice(self, invoice_nbr: str) -> Optional[Invoice]:
        """Search for an invoice by number."""
        for invoice in self.invoices:
            if invoice.invoice_nbr == invoice_nbr:
                return invoice
        return None

    def get_all_invoices(self) -> List[Invoice]:
        """Return all invoices in the repository."""
        return self.invoices.copy()

    def get_invoice_count(self) -> int:
        """Return the total number of invoices."""
        return len(self.invoices)

def test_inheritance_system():
    """Test function to verify inheritance functionality."""
    # Test Person and Customer inheritance
    customer = Customer("John Doe", "123-456-7890", "john@example.com")
    print("\n=== Testing Person/Customer Inheritance ===")
    print(f"Name (from Person): {customer.name}")
    print(f"Phone (from Person): {customer.phone}")
    print(f"Email (from Person): {customer.email}")
    print(f"Is customer instance of Person? {isinstance(customer, Person)}")

    # Test Product and Stock inheritance
    stock = Stock("Python Programming", "John Smith", 29.99)
    print("\n=== Testing Product/Stock Inheritance ===")
    print(f"Name (from Product): {stock.name}")
    print(f"Price (from Product): £{stock.price:.2f}")
    print(f"Author (from Stock): {stock.author}")
    print(f"Book name (from Stock): {stock.book_name}")
    print(f"Is stock instance of Product? {isinstance(stock, Product)}")

    # Test complete order flow with inherited classes
    print("\n=== Testing Complete Order Flow ===")
    order = Order(customer, stock)
    shipping = Shipping(order, datetime.now())
    shipping.set_ship_cost(True)  # Test urgent shipping
    
    invoice = Invoice("INV001", stock, shipping)
    invoice.calculate_total()
    
    print(f"Customer Name: {order.customer.name}")
    print(f"Book: {order.stock.book_name}")
    print(f"Author: {order.stock.author}")
    print(f"Book Price: £{order.stock.price:.2f}")
    print(f"Shipping Cost: £{shipping.calc_ship_cost():.2f}")
    print(f"Total Cost: £{invoice.total_cost:.2f}")

if __name__ == "__main__":
    test_inheritance_system() 