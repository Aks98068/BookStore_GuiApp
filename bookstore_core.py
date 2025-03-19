"""
Book Ordering System - Core Classes
This module contains the core classes for the book ordering system without inheritance.
"""

from datetime import datetime
from typing import Optional, List

class Customer:
    """Customer class to store customer information."""
    def __init__(self, name: str, phone: str, email: str):
        self._name = name
        self._phone = phone
        self._email = email

    @property
    def name(self) -> str:
        """Get customer name."""
        return self._name

    @property
    def phone(self) -> str:
        """Get customer phone number."""
        return self._phone

    @property
    def email(self) -> str:
        """Get customer email."""
        return self._email

class Stock:
    """Stock class to manage book inventory."""
    def __init__(self, book_name: str, author: str, price: float):
        self._book_name = book_name
        self._author = author
        self._price = price

    @property
    def book_name(self) -> str:
        """Get book name."""
        return self._book_name

    @property
    def author(self) -> str:
        """Get book author."""
        return self._author

    @property
    def price(self) -> float:
        """Get book price."""
        return self._price

class Order:
    """Order class to link customer with their book purchase."""
    def __init__(self, customer: Customer, stock: Stock):
        self.customer = customer
        self.stock = stock

class Shipping:
    """Shipping class to handle delivery details and costs."""
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
    """Invoice class to generate and manage order invoices."""
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
    """BookStore class to manage the overall system."""
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

def test_book_ordering_system():
    """Test function to verify all system functionalities."""
    # Create test customers
    customers = [
        Customer("John Doe", "123-456-7890", "john@example.com"),
        Customer("Jane Smith", "098-765-4321", "jane@example.com"),
        Customer("Bob Wilson", "111-222-3333", "bob@example.com")
    ]

    # Create test stock items
    stocks = [
        Stock("Python Programming", "John Smith", 29.99),
        Stock("Data Science Basics", "Mary Johnson", 39.99),
        Stock("Web Development", "David Brown", 34.99)
    ]

    # Create test orders
    orders = [
        Order(customers[0], stocks[0]),
        Order(customers[1], stocks[1]),
        Order(customers[2], stocks[2])
    ]

    # Create test shipping orders
    shipping_orders = [
        Shipping(orders[0], datetime.now()),
        Shipping(orders[1], datetime.now()),
        Shipping(orders[2], datetime.now())
    ]

    # Test shipping costs
    shipping_orders[0].set_ship_cost(True)  # Urgent shipping
    shipping_orders[1].set_ship_cost(False)  # Standard shipping
    shipping_orders[2].set_ship_cost(True)  # Urgent shipping

    # Create test invoices
    invoices = [
        Invoice("INV001", stocks[0], shipping_orders[0]),
        Invoice("INV002", stocks[1], shipping_orders[1]),
        Invoice("INV003", stocks[2], shipping_orders[2])
    ]

    # Calculate totals
    for invoice in invoices:
        invoice.calculate_total()

    # Create BookStore and add invoices
    bookstore = BookStore()
    for invoice in invoices:
        bookstore.add_invoice(invoice)

    # Test output
    print("\n=== Test Results ===")
    
    print("\nCustomers:")
    for customer in customers:
        print(f"Name: {customer.name}, Phone: {customer.phone}, Email: {customer.email}")

    print("\nBooks in Stock:")
    for stock in stocks:
        print(f"Book: {stock.book_name}, Author: {stock.author}, Price: £{stock.price:.2f}")

    print("\nShipping Costs:")
    for i, shipping in enumerate(shipping_orders):
        print(f"Order {i+1}: £{shipping.calc_ship_cost():.2f}")

    print("\nInvoices:")
    for invoice in invoices:
        print(f"Invoice {invoice.invoice_nbr}:")
        print(f"Book: {invoice.stock.book_name}")
        print(f"Customer: {invoice.ship_order.order.customer.name}")
        print(f"Total Cost: £{invoice.total_cost:.2f}\n")

    # Test invoice search
    test_invoice = bookstore.search_invoice("INV001")
    if test_invoice:
        print("Invoice Search Test:")
        print(f"Found Invoice {test_invoice.invoice_nbr} - Total: £{test_invoice.total_cost:.2f}")

if __name__ == "__main__":
    test_book_ordering_system() 