"""
Book Ordering System - GUI Implementation
This module contains the Tkinter-based GUI implementation of the book ordering system.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from bookstore_core_inher import Customer, Stock, Order, Shipping, Invoice, BookStore

class BookOrderingSystemGUI:
    """Main GUI class for the Book Ordering System."""
    
    def __init__(self, root):
        """Initialize the GUI with main window and tabs."""
        self.root = root
        self.root.title("Book Ordering System")
        self.root.geometry("800x600")
        
        # Initialize BookStore
        self.bookstore = BookStore()
        
        # Data storage
        self.customers = []
        self.stocks = []
        
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Create tabs
        self.create_customer_tab()
        self.create_book_tab()
        self.create_order_tab()
        self.create_invoice_tab()

    def create_customer_tab(self):
        """Create the Customer Management tab."""
        customer_frame = ttk.Frame(self.notebook)
        self.notebook.add(customer_frame, text="Customer Management")
        
        # Customer input fields
        ttk.Label(customer_frame, text="Customer Details", font=('Helvetica', 12, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(customer_frame)
        input_frame.pack(fill='x', padx=20)
        
        # Name field
        ttk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.customer_name = ttk.Entry(input_frame)
        self.customer_name.grid(row=0, column=1, padx=5, pady=5)
        
        # Phone field
        ttk.Label(input_frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        self.customer_phone = ttk.Entry(input_frame)
        self.customer_phone.grid(row=1, column=1, padx=5, pady=5)
        
        # Email field
        ttk.Label(input_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.customer_email = ttk.Entry(input_frame)
        self.customer_email.grid(row=2, column=1, padx=5, pady=5)
        
        # Add button
        ttk.Button(input_frame, text="Add Customer", command=self.add_customer).grid(row=3, column=0, columnspan=2, pady=10)

    def create_book_tab(self):
        """Create the Book Management tab."""
        book_frame = ttk.Frame(self.notebook)
        self.notebook.add(book_frame, text="Book Management")
        
        ttk.Label(book_frame, text="Book Details", font=('Helvetica', 12, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(book_frame)
        input_frame.pack(fill='x', padx=20)
        
        # Book name field
        ttk.Label(input_frame, text="Book Name:").grid(row=0, column=0, padx=5, pady=5)
        self.book_name = ttk.Entry(input_frame)
        self.book_name.grid(row=0, column=1, padx=5, pady=5)
        
        # Author field
        ttk.Label(input_frame, text="Author:").grid(row=1, column=0, padx=5, pady=5)
        self.book_author = ttk.Entry(input_frame)
        self.book_author.grid(row=1, column=1, padx=5, pady=5)
        
        # Price field
        ttk.Label(input_frame, text="Price:").grid(row=2, column=0, padx=5, pady=5)
        self.book_price = ttk.Entry(input_frame)
        self.book_price.grid(row=2, column=1, padx=5, pady=5)
        
        # Add button
        ttk.Button(input_frame, text="Add Book", command=self.add_book).grid(row=3, column=0, columnspan=2, pady=10)

    def create_order_tab(self):
        """Create the Order Management tab."""
        order_frame = ttk.Frame(self.notebook)
        self.notebook.add(order_frame, text="Order Management")
        
        ttk.Label(order_frame, text="Place Order", font=('Helvetica', 12, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(order_frame)
        input_frame.pack(fill='x', padx=20)
        
        # Customer selection
        ttk.Label(input_frame, text="Select Customer:").grid(row=0, column=0, padx=5, pady=5)
        self.customer_var = tk.StringVar()
        self.customer_dropdown = ttk.Combobox(input_frame, textvariable=self.customer_var)
        self.customer_dropdown.grid(row=0, column=1, padx=5, pady=5)
        
        # Book selection
        ttk.Label(input_frame, text="Select Book:").grid(row=1, column=0, padx=5, pady=5)
        self.book_var = tk.StringVar()
        self.book_dropdown = ttk.Combobox(input_frame, textvariable=self.book_var)
        self.book_dropdown.grid(row=1, column=1, padx=5, pady=5)
        
        # Shipping options
        self.urgent_shipping = tk.BooleanVar()
        ttk.Checkbutton(input_frame, text="Urgent Shipping", variable=self.urgent_shipping).grid(row=2, column=0, columnspan=2, pady=5)
        
        # Place order button
        ttk.Button(input_frame, text="Place Order", command=self.place_order).grid(row=3, column=0, columnspan=2, pady=10)

    def create_invoice_tab(self):
        """Create the Invoice Management tab."""
        invoice_frame = ttk.Frame(self.notebook)
        self.notebook.add(invoice_frame, text="Invoice Management")
        
        ttk.Label(invoice_frame, text="Invoice Management", font=('Helvetica', 12, 'bold')).pack(pady=10)
        
        # Invoice search
        search_frame = ttk.Frame(invoice_frame)
        search_frame.pack(fill='x', padx=20)
        
        ttk.Label(search_frame, text="Invoice Number:").grid(row=0, column=0, padx=5, pady=5)
        self.invoice_search = ttk.Entry(search_frame)
        self.invoice_search.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(search_frame, text="Search Invoice", command=self.search_invoice).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(search_frame, text="View All Invoices", command=self.view_all_invoices).grid(row=1, column=0, columnspan=3, pady=10)
        
        # Results area
        self.invoice_text = tk.Text(invoice_frame, height=10, width=50)
        self.invoice_text.pack(pady=10, padx=20)

    def add_customer(self):
        """Add a new customer to the system."""
        name = self.customer_name.get()
        phone = self.customer_phone.get()
        email = self.customer_email.get()
        
        if name and phone and email:
            customer = Customer(name, phone, email)
            self.customers.append(customer)
            self.update_customer_dropdown()
            messagebox.showinfo("Success", "Customer added successfully!")
            # Clear fields
            self.customer_name.delete(0, tk.END)
            self.customer_phone.delete(0, tk.END)
            self.customer_email.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill all customer details!")

    def add_book(self):
        """Add a new book to the system."""
        name = self.book_name.get()
        author = self.book_author.get()
        try:
            price = float(self.book_price.get())
            if name and author:
                stock = Stock(name, author, price)
                self.stocks.append(stock)
                self.update_book_dropdown()
                messagebox.showinfo("Success", "Book added successfully!")
                # Clear fields
                self.book_name.delete(0, tk.END)
                self.book_author.delete(0, tk.END)
                self.book_price.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please fill all book details!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price!")

    def update_customer_dropdown(self):
        """Update the customer selection dropdown."""
        self.customer_dropdown['values'] = [customer.name for customer in self.customers]

    def update_book_dropdown(self):
        """Update the book selection dropdown."""
        self.book_dropdown['values'] = [stock.book_name for stock in self.stocks]

    def place_order(self):
        """Place a new order in the system."""
        customer_name = self.customer_var.get()
        book_name = self.book_var.get()
        
        if not customer_name or not book_name:
            messagebox.showerror("Error", "Please select both customer and book!")
            return
        
        customer = next((c for c in self.customers if c.name == customer_name), None)
        stock = next((s for s in self.stocks if s.book_name == book_name), None)
        
        if customer and stock:
            order = Order(customer, stock)
            shipping = Shipping(order, datetime.now())
            shipping.set_ship_cost(self.urgent_shipping.get())
            
            invoice_nbr = f"INV{self.bookstore.get_invoice_count() + 1:03d}"
            invoice = Invoice(invoice_nbr, stock, shipping)
            invoice.calculate_total()
            
            self.bookstore.add_invoice(invoice)
            messagebox.showinfo("Success", f"Order placed successfully!\nInvoice Number: {invoice_nbr}\nTotal Cost: £{invoice.total_cost:.2f}")
        else:
            messagebox.showerror("Error", "Invalid customer or book selection!")

    def search_invoice(self):
        """Search for an invoice by number."""
        invoice_nbr = self.invoice_search.get()
        if not invoice_nbr:
            messagebox.showerror("Error", "Please enter an invoice number!")
            return
            
        invoice = self.bookstore.search_invoice(invoice_nbr)
        if invoice:
            self.display_invoice(invoice)
        else:
            messagebox.showerror("Error", "Invoice not found!")

    def view_all_invoices(self):
        """Display all invoices in the system."""
        invoices = self.bookstore.get_all_invoices()
        if not invoices:
            messagebox.showinfo("Info", "No invoices found!")
            return
            
        self.invoice_text.delete(1.0, tk.END)
        for invoice in invoices:
            self.display_invoice(invoice, append=True)

    def display_invoice(self, invoice, append=False):
        """Display invoice details in the text area."""
        if not append:
            self.invoice_text.delete(1.0, tk.END)
            
        invoice_text = f"""
Invoice Number: {invoice.invoice_nbr}
Customer: {invoice.ship_order.order.customer.name}
Book: {invoice.stock.book_name}
Author: {invoice.stock.author}
Price: £{invoice.stock.price:.2f}
Shipping Cost: £{invoice.ship_order.calc_ship_cost():.2f}
Total Cost: £{invoice.total_cost:.2f}
{'='*50}
"""
        self.invoice_text.insert(tk.END, invoice_text)

def main():
    """Main function to start the GUI application."""
    root = tk.Tk()
    app = BookOrderingSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 