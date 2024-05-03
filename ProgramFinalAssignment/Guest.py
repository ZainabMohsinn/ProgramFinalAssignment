import tkinter as tk
from tkinter import ttk, messagebox

# Define a base class for a Person
class Person:
    def __init__(self, name=""):
        self.name = name

# Define a subclass Guest, inheriting from Person
class Guest(Person):
    def __init__(self, name="", id="", address="", contactDetails=""):
        super().__init__(name)
        self.id = id
        self.address = address
        self.contactDetails = contactDetails

# Define the GUI for managing guests
class GuestManagerGUI:
    def __init__(self):
        # Initialize list to store guest objects
        self.guests = []

        # Create main window
        self.root = tk.Tk()
        self.root.title("Guest Manager")

        # Create a table to display guest information
        self.table = ttk.Treeview(self.root, columns=('Name', 'ID', 'Address', 'Contact Details'))
        self.table.heading('Name', text='Name')
        self.table.heading('ID', text='ID')
        self.table.heading('Address', text='Address')
        self.table.heading('Contact Details', text='Contact Details')
        self.table.pack(padx=10, pady=10)

        # Buttons for various operations
        self.add_button = tk.Button(self.root, text="Add Guest", command=self.add_guest_window)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Guest", command=self.delete_guest)
        self.delete_button.pack(pady=5)

        self.modify_button = tk.Button(self.root, text="Modify Guest", command=self.modify_guest_window)
        self.modify_button.pack(pady=5)

        self.display_button = tk.Button(self.root, text="Display Guest Details",
                                        command=self.display_guest_details)
        self.display_button.pack(pady=5)

        # Display existing guests
        self.display_guests()

        self.root.mainloop()

    # Function to create a window for adding a new guest
    def add_guest_window(self):
        add_window = tk.Toplevel()
        add_window.title("Add Guest")

        # Labels and entry fields for guest details
        labels = ['Name', 'ID', 'Address', 'Contact Details']
        entries = []

        for i, label in enumerate(labels):
            tk.Label(add_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        # Button to add the guest
        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_guest(entries))
        add_button.grid(row=len(labels), column=1, padx=5, pady=5)

    # Function to add a new guest
    def add_guest(self, entries):
        try:
            values = [entry.get() for entry in entries]
            if not values[0] or not values[1]:
                raise ValueError("Name and ID are required fields.")

            for guest in self.guests:
                if guest.id == values[1]:
                    raise ValueError("Guest ID already exists.")

            # Create new guest object and add to the list
            guest = Guest(name=values[0], id=values[1], address=values[2], contactDetails=values[3])
            self.guests.append(guest)
            self.display_guests()
            self.clear_entries(entries)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to clear entry fields
    def clear_entries(self, entries):
        for entry in entries:
            entry.delete(0, tk.END)

    # Function to delete a guest
    def delete_guest(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select a guest to delete.")

            item = self.table.item(selected_item)
            guest_id = item['values'][1]
            for guest in self.guests:
                if guest.id == guest_id:
                    self.guests.remove(guest)
                    break
            self.display_guests()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to create a window for modifying guest details
    def modify_guest_window(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select a guest to modify.")

            item = self.table.item(selected_item)
            guest_id = item['values'][1]
            for guest in self.guests:
                if guest.id == guest_id:
                    modify_window = tk.Toplevel()
                    modify_window.title("Modify Guest")

                    # Labels and entry fields pre-filled with existing guest details
                    labels = ['Name', 'ID', 'Address', 'Contact Details']
                    entries = []

                    for i, label in enumerate(labels):
                        tk.Label(modify_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        entry = tk.Entry(modify_window)
                        entry.grid(row=i, column=1, padx=5, pady=5)
                        entry.insert(tk.END, guest.__dict__[label.lower().replace(' ', '')])
                        entries.append(entry)

                    # Button to modify the guest
                    modify_button = tk.Button(modify_window, text="Modify",
                                              command=lambda: self.modify_guest(guest, entries, modify_window))
                    modify_button.grid(row=len(labels), column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to modify guest details
    def modify_guest(self, guest, entries, modify_window):
        try:
            values = [entry.get() for entry in entries]
            if not values[0] or not values[1]:
                raise ValueError("Name and ID are required fields.")

            for g in self.guests:
                if g.id == values[1] and g != guest:
                    raise ValueError("Guest ID already exists.")

            # Update guest details
            guest.name = values[0]
            guest.id = values[1]
            guest.address = values[2]
            guest.contactDetails = values[3]

            self.display_guests()
            modify_window.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display details of a selected guest
    def display_guest_details(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select a guest to display details.")

            item = self.table.item(selected_item)
            guest_id = item['values'][1]
            for guest in self.guests:
                if guest.id == guest_id:
                    details_window = tk.Toplevel()
                    details_window.title("Guest Details")

                    # Display guest details
                    labels = ['Name', 'ID', 'Address', 'Contact Details']
                    for i, label in enumerate(labels):
                        tk.Label(details_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        tk.Label(details_window, text=guest.__dict__[label.lower().replace(' ', '')]).grid(row=i, column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display all guests in the table
    def display_guests(self):
        # Clear the table
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert guests into the table
        for guest in self.guests:
            self.table.insert('', 'end', values=(
                guest.name, guest.id, guest.address, guest.contactDetails))

# Run the GUI
GuestManagerGUI()
