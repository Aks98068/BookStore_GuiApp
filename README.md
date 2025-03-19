<<<<<<< HEAD
# Book Ordering System

A Python-based Book Ordering System implementing Object-Oriented Programming principles, inheritance, and a Tkinter-based GUI interface.

## Project Overview

This system demonstrates the implementation of OOP concepts including:
- Encapsulation using private attributes and property decorators
- Inheritance with base and derived classes
- Clean code practices with proper documentation
- Modern GUI design using Tkinter

## Project Structure

The project is organized into three main Python files:

1. `bookstore_core.py`: Contains the basic implementation without inheritance
   - Customer, Stock, Order, Shipping, Invoice, and BookStore classes
   - Test cases for basic functionality

2. `bookstore_core_inher.py`: Implements the inheritance structure
   - Person (base) → Customer (derived)
   - Product (base) → Stock (derived)
   - Enhanced test cases demonstrating inheritance

3. `bookstore_gui.py`: Tkinter-based GUI implementation
   - Uses the inheritance-based classes
   - Provides a user-friendly interface for all operations

## Class Hierarchy

### Basic Implementation (bookstore_core.py)
- Customer
- Stock
- Order
- Shipping
- Invoice
- BookStore

### Inheritance Implementation (bookstore_core_inher.py)
- Person (Base Class)
  - Customer
- Product (Base Class)
  - Stock
- Order
- Shipping
- Invoice
- BookStore

## Features

### 1. Customer Management
- Add new customers with:
  - Name
  - Phone number
  - Email address
- Property-based getters for encapsulation

### 2. Book Stock Management
- Add books with:
  - Book name
  - Author
  - Price
- Inheritance-based implementation from Product class

### 3. Order Processing
- Create orders linking customers with books
- Flexible shipping options:
  - Standard shipping (£3.95)
  - Urgent shipping (£5.45)
- Automatic shipping cost calculation

### 4. Invoice Management
- Automatic invoice generation
- Total cost calculation (book price + shipping)
- Invoice search functionality
- View all invoices option

## GUI Interface

The GUI is organized into four main tabs:

1. Customer Management Tab
   - Add new customers
   - Input validation
   - Success/error feedback

2. Book Management Tab
   - Add new books
   - Price validation
   - Success/error feedback

3. Order Management Tab
   - Customer selection dropdown
   - Book selection dropdown
   - Shipping option checkbox
   - Order placement

4. Invoice Management Tab
   - Invoice search by number
   - View all invoices
   - Detailed invoice display

## Installation

1. Ensure you have Python 3.x installed
2. No additional dependencies required (uses built-in Tkinter)

## Running the Application

1. Start the GUI application:
```bash
python bookstore_gui.py
```

2. Run the basic implementation tests:
```bash
python bookstore_core.py
```

3. Run the inheritance implementation tests:
```bash
python bookstore_core_inher.py
```

## Usage Guide

1. Adding a Customer:
   - Go to Customer Management tab
   - Fill in name, phone, and email
   - Click "Add Customer"
   - Verify success message

2. Adding a Book:
   - Go to Book Management tab
   - Enter book name, author, and price
   - Click "Add Book"
   - Verify success message

3. Placing an Order:
   - Go to Order Management tab
   - Select customer from dropdown
   - Select book from dropdown
   - Choose shipping option
   - Click "Place Order"
   - Note the invoice number

4. Managing Invoices:
   - Go to Invoice Management tab
   - Search by invoice number
   - Or view all invoices
   - Review invoice details

## Implementation Notes

- Uses @property decorators for getter methods
- Implements proper encapsulation with private attributes
- Demonstrates inheritance with Person and Product base classes
- Includes comprehensive error handling
- Features a modern, user-friendly GUI interface

## Testing

The system includes two test modules:
1. Basic functionality tests in `bookstore_core.py`
2. Inheritance tests in `bookstore_core_inher.py`

Both test modules provide console output to verify:
- Object creation
- Inheritance relationships
- Business logic
- Cost calculations 
=======
# BookStore_GuiApp
>>>>>>> 474b53b043eaa6cd1ad4082eb10cd5119173cdaa
