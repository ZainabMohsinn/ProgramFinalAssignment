import tkinter as tk
from tkinter import ttk, messagebox

# Define a base class for suppliers
class Supplier:
    def __init__(self, name, supplier_id, address, contact_details):
        self.name = name
        self.supplier_id = supplier_id
        self.address = address
        self.contact_details = contact_details

# Define the GUI for managing suppliers
class SupplierManagerGUI:
    def __init__(self):
        # Initialize list to store supplier objects
        self.suppliers = []

        # Create main window
        self.root = tk.Tk()
        self.root.title("Supplier Manager")

        # Create a table to display supplier information
        self.supplier_table = ttk.Treeview(self.root, columns=('Name', 'ID', 'Address', 'Contact Details'))
        self.supplier_table.heading('Name', text='Name')
        self.supplier_table.heading('ID', text='ID')
        self.supplier_table.heading('Address', text='Address')
        self.supplier_table.heading('Contact Details', text='Contact Details')
        self.supplier_table.pack(padx=10, pady=10)

        # Buttons for various operations
        self.add_supplier_button = tk.Button(self.root, text="Add Supplier", command=self.add_supplier_window)
        self.add_supplier_button.pack(pady=5)

        self.delete_supplier_button = tk.Button(self.root, text="Delete Supplier", command=self.delete_supplier)
        self.delete_supplier_button.pack(pady=5)

        self.modify_supplier_button = tk.Button(self.root, text="Modify Supplier", command=self.modify_supplier_window)
        self.modify_supplier_button.pack(pady=5)

        self.display_supplier_button = tk.Button(self.root, text="Display Supplier Details", command=self.display_supplier_details)
        self.display_supplier_button.pack(pady=5)

        # Display existing suppliers
        self.display_suppliers()

        self.root.mainloop()

    # Function to create a window for adding a new supplier
    def add_supplier_window(self):
        add_window = tk.Toplevel()
        add_window.title("Add Supplier")

        # Labels and entry fields for supplier details
        labels = ['Name', 'ID', 'Address', 'Contact Details']
        entries = []

        for i, label in enumerate(labels):
            tk.Label(add_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        # Button to add the supplier
        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_supplier(entries))
        add_button.grid(row=len(labels), column=1, padx=5, pady=5)

    # Function to add a new supplier
    def add_supplier(self, entries):
        try:
            values = [entry.get() for entry in entries]
            if not values[0]:
                raise ValueError("Name is a required field.")

            for supplier in self.suppliers:
                if supplier.name == values[0]:
                    raise ValueError("Supplier with this name already exists.")

            # Create new supplier object and add to the list
            supplier = Supplier(*values)
            self.suppliers.append(supplier)
            self.display_suppliers()
            self.clear_entries(entries)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to clear entry fields
    def clear_entries(self, entries):
        for entry in entries:
            entry.delete(0, tk.END)

    # Function to delete a supplier
    def delete_supplier(self):
        try:
            selected_item = self.supplier_table.selection()
            if not selected_item:
                raise ValueError("Please select a supplier to delete.")

            item = self.supplier_table.item(selected_item)
            name = item['values'][0]
            for supplier in self.suppliers:
                if supplier.name == name:
                    self.suppliers.remove(supplier)
                    break
            self.display_suppliers()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to create a window for modifying supplier details
    def modify_supplier_window(self):
        try:
            selected_item = self.supplier_table.selection()
            if not selected_item:
                raise ValueError("Please select a supplier to modify.")

            item = self.supplier_table.item(selected_item)
            name = item['values'][0]
            for supplier in self.suppliers:
                if supplier.name == name:
                    modify_window = tk.Toplevel()
                    modify_window.title("Modify Supplier")

                    # Labels and entry fields pre-filled with existing supplier details
                    labels = ['Name', 'ID', 'Address', 'Contact Details']
                    entries = []

                    for i, label in enumerate(labels):
                        tk.Label(modify_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        entry = tk.Entry(modify_window)
                        entry.grid(row=i, column=1, padx=5, pady=5)
                        entry.insert(tk.END, supplier.__dict__[label.lower().replace(' ', '_')])
                        entries.append(entry)

                    # Button to modify the supplier
                    modify_button = tk.Button(modify_window, text="Modify",
                                              command=lambda: self.modify_supplier(supplier, entries, modify_window))
                    modify_button.grid(row=len(labels), column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to modify supplier details
    def modify_supplier(self, supplier, entries, modify_window):
        try:
            values = [entry.get() for entry in entries]
            if not values[0]:
                raise ValueError("Name is a required field.")

            for s in self.suppliers:
                if s.name == values[0] and s != supplier:
                    raise ValueError("Supplier with this name already exists.")

            # Update supplier details
            supplier.name = values[0]
            supplier.supplier_id = values[1]
            supplier.address = values[2]
            supplier.contact_details = values[3]

            self.display_suppliers()
            modify_window.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display details of a selected supplier
    def display_supplier_details(self):
        try:
            selected_item = self.supplier_table.selection()
            if not selected_item:
                raise ValueError("Please select a supplier to display details.")

            item = self.supplier_table.item(selected_item)
            name = item['values'][0]
            for supplier in self.suppliers:
                if supplier.name == name:
                    details_window = tk.Toplevel()
                    details_window.title("Supplier Details")

                    # Display supplier details
                    labels = ['Name', 'ID', 'Address', 'Contact Details']
                    for i, label in enumerate(labels):
                        tk.Label(details_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        tk.Label(details_window, text=supplier.__dict__[label.lower().replace(' ', '_')]).grid(row=i, column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display all suppliers in the table
    def display_suppliers(self):
        # Clear the table
        for item in self.supplier_table.get_children():
            self.supplier_table.delete(item)

        # Insert suppliers into the table
        for supplier in self.suppliers:
            self.supplier_table.insert('', 'end', values=(
                supplier.name, supplier.supplier_id, supplier.address, supplier.contact_details))

# Run the GUI
SupplierManagerGUI()
