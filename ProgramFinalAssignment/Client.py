import tkinter as tk
from tkinter import ttk


class Person:
    def __init__(self, name=""):
        self.name = name


class Client(Person):
    def __init__(self, name="", client_id="", address="", contact_details="", budget=""):
        super().__init__(name)
        self.client_id = client_id
        self.address = address
        self.contact_details = contact_details
        self.budget = budget
        self.events = []  # Composition: client has multiple events as a list


class ClientManagerGUI:
    def __init__(self):
        # Initialize list to store client objects
        self.clients = []

        # Create main window
        self.root = tk.Tk()
        self.root.title("Client Manager")

        # Create a table to display client information
        self.table = ttk.Treeview(self.root, columns=('Name', 'ID', 'Address', 'Contact Details', 'Budget'))
        self.table.heading('Name', text='Name')
        self.table.heading('ID', text='ID')
        self.table.heading('Address', text='Address')
        self.table.heading('Contact Details', text='Contact Details')
        self.table.heading('Budget', text='Budget')
        self.table.pack(padx=10, pady=10)

        # Buttons for various operations
        self.add_button = tk.Button(self.root, text="Add Client", command=self.add_client_window)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Client", command=self.delete_client)
        self.delete_button.pack(pady=5)

        self.modify_button = tk.Button(self.root, text="Modify Client", command=self.modify_client_window)
        self.modify_button.pack(pady=5)

        self.display_button = tk.Button(self.root, text="Display Client Details", command=self.display_client_details)
        self.display_button.pack(pady=5)

        # Display existing clients in the table
        self.display_clients()

        self.root.mainloop()

    def add_client_window(self):
        """Create a window for adding a new client."""
        add_window = tk.Toplevel()
        add_window.title("Add Client")

        # Entry fields for client details
        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="ID:").grid(row=1, column=0, padx=5, pady=5)
        id_entry = tk.Entry(add_window)
        id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        address_entry = tk.Entry(add_window)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        contact_entry = tk.Entry(add_window)
        contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Budget:").grid(row=4, column=0, padx=5, pady=5)
        budget_entry = tk.Entry(add_window)
        budget_entry.grid(row=4, column=1, padx=5, pady=5)

        # Button to add the client
        add_button = tk.Button(add_window, text="Add",
                               command=lambda: self.add_client(name_entry.get(), id_entry.get(), address_entry.get(),
                                                               contact_entry.get(), budget_entry.get(), add_window))
        add_button.grid(row=5, column=1, padx=5, pady=5)

    def add_client(self, name, client_id, address, contact_details, budget, add_window):
        """Add a new client."""
        try:
            if not name or not client_id:
                raise ValueError("Name and ID are required fields.")

            # Check if client ID already exists
            for client in self.clients:
                if client.client_id == client_id:
                    raise ValueError("Client ID already exists.")

            # Create new client object and add to the list
            self.clients.append(Client(name, client_id, address, contact_details, budget))
            # Update the table with the new client
            self.display_clients()
            # Close the add window
            add_window.destroy()
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def delete_client(self):
        """Delete a client."""
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select a client to delete.")

            # Get the client ID of the selected client
            item = self.table.item(selected_item)
            client_id = item['values'][1]

            # Find and remove the client from the list
            for client in self.clients:
                if client.client_id == client_id:
                    self.clients.remove(client)
                    break

            # Update the table after deletion
            self.display_clients()
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def modify_client_window(self):
        """Create a window for modifying client details."""
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select a client to modify.")

            # Get the client ID of the selected client
            item = self.table.item(selected_item)
            client_id = item['values'][1]

            # Find the selected client
            for client in self.clients:
                if client.client_id == client_id:
                    # Create a modify window
                    modify_window = tk.Toplevel()
                    modify_window.title("Modify Client")

                    # Entry fields pre-filled with existing client details
                    tk.Label(modify_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
                    name_entry = tk.Entry(modify_window)
                    name_entry.grid(row=0, column=1, padx=5, pady=5)
                    name_entry.insert(tk.END, client.name)

                    tk.Label(modify_window, text="ID:").grid(row=1, column=0, padx=5, pady=5)
                    id_entry = tk.Entry(modify_window)
                    id_entry.grid(row=1, column=1, padx=5, pady=5)
                    id_entry.insert(tk.END, client.client_id)

                    tk.Label(modify_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
                    address_entry = tk.Entry(modify_window)
                    address_entry.grid(row=2, column=1, padx=5, pady=5)
                    address_entry.insert(tk.END, client.address)

                    tk.Label(modify_window, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
                    contact_entry = tk.Entry(modify_window)
                    contact_entry.grid(row=3, column=1, padx=5, pady=5)
                    contact_entry.insert(tk.END, client.contact_details)

                    tk.Label(modify_window, text="Budget:").grid(row=4, column=0, padx=5, pady=5)
                    budget_entry = tk.Entry(modify_window)
                    budget_entry.grid(row=4, column=1, padx=5, pady=5)
                    budget_entry.insert(tk.END, client.budget)

                    # Button to modify the client
                    modify_button = tk.Button(modify_window, text="Modify",
                                              command=lambda: self.modify_client(client, name_entry.get(),
                                                                                 id_entry.get(), address_entry.get(),
                                                                                 contact_entry.get(),
                                                                                 budget_entry.get(), modify_window))
                    modify_button.grid(row=5, column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def modify_client(self, client, name, client_id, address, contact_details, budget, modify_window):
        """Modify client details."""
        try:
            if not name or not client_id:
                raise ValueError("Name and ID are required fields.")

            # Check if new client ID already exists
            for c in self.clients:
                if c.client_id == client_id and c != client:
                    raise ValueError("Client ID already exists.")

            # Update client details
            client.name = name
            client.client_id = client_id
            client.address = address
            client.contact_details = contact_details
            client.budget = budget

            # Update the table with modified details
            self.display_clients()
            modify_window.destroy()  # Close the modify window
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def display_client_details(self):
        """Display details of a selected client."""
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select a client to display details.")

            # Get the client ID of the selected client
            item = self.table.item(selected_item)
            client_id = item['values'][1]

            # Find the selected client
            for client in self.clients:
                if client.client_id == client_id:
                    # Create a details window
                    details_window = tk.Toplevel()
                    details_window.title("Client Details")

                    # Display client details
                    tk.Label(details_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
                    tk.Label(details_window, text=client.name).grid(row=0, column=1, padx=5, pady=5)

                    tk.Label(details_window, text="ID:").grid(row=1, column=0, padx=5, pady=5)
                    tk.Label(details_window, text=client.client_id).grid(row=1, column=1, padx=5, pady=5)

                    tk.Label(details_window, text="Address:").grid(row=2, column=0, padx=5, pady=5)
                    tk.Label(details_window, text=client.address).grid(row=2, column=1, padx=5, pady=5)

                    tk.Label(details_window, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
                    tk.Label(details_window, text=client.contact_details).grid(row=3, column=1, padx=5, pady=5)

                    tk.Label(details_window, text="Budget:").grid(row=4, column=0, padx=5, pady=5)
                    tk.Label(details_window, text=client.budget).grid(row=4, column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def display_clients(self):
        """Display all clients in the table."""
        # Clear the table
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert clients into the table
        for client in self.clients:
            self.table.insert('', 'end', values=(
                client.name, client.client_id, client.address, client.contact_details, client.budget))


# Run the GUI
ClientManagerGUI()
