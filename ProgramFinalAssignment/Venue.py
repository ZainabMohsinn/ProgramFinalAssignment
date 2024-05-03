import tkinter as tk
from tkinter import ttk, messagebox

# Define a class for managing venues
class Venue:
    def __init__(self, venueId="", name="", address="", contact="", minGuests="", maxGuests=""):
        self.venueId = venueId
        self.name = name
        self.address = address
        self.contact = contact
        self.minGuests = minGuests
        self.maxGuests = maxGuests

# Define the GUI for managing venues
class VenueManagerGUI:
    def __init__(self):
        self.venues = []  # List to store venues
        self.root = tk.Tk()
        self.root.title("Venue Manager")

        # Define the Treeview for venues
        self.venue_table = ttk.Treeview(self.root, columns=('Venue ID', 'Name', 'Address', 'Contact', 'Min Guests', 'Max Guests'))
        self.venue_table.heading('Venue ID', text='Venue ID')
        self.venue_table.heading('Name', text='Name')
        self.venue_table.heading('Address', text='Address')
        self.venue_table.heading('Contact', text='Contact')
        self.venue_table.heading('Min Guests', text='Min Guests')
        self.venue_table.heading('Max Guests', text='Max Guests')
        self.venue_table.pack(padx=10, pady=10)

        # Buttons for venue operations
        self.add_venue_button = tk.Button(self.root, text="Add Venue", command=self.add_venue_window)
        self.add_venue_button.pack(pady=5)

        self.delete_venue_button = tk.Button(self.root, text="Delete Venue", command=self.delete_venue)
        self.delete_venue_button.pack(pady=5)

        self.modify_venue_button = tk.Button(self.root, text="Modify Venue", command=self.modify_venue_window)
        self.modify_venue_button.pack(pady=5)

        self.display_venue_button = tk.Button(self.root, text="Display Venue Details", command=self.display_venue_details)
        self.display_venue_button.pack(pady=5)

        # Display existing venues
        self.display_venues()

        self.root.mainloop()

    # Function to create a window for adding a new venue
    def add_venue_window(self):
        add_window = tk.Toplevel()
        add_window.title("Add Venue")

        # Labels and entry fields for venue details
        labels = ['Venue ID', 'Name', 'Address', 'Contact', 'Min Guests', 'Max Guests']
        entries = []

        for i, label in enumerate(labels):
            tk.Label(add_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        # Button to add the venue
        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_venue(entries))
        add_button.grid(row=len(labels), column=1, padx=5, pady=5)

    # Function to add a new venue
    def add_venue(self, entries):
        try:
            values = [entry.get() for entry in entries]
            # Validate required fields
            if not values[0]:
                raise ValueError("Venue ID is a required field.")

            for venue in self.venues:
                if venue.venueId == values[0]:
                    raise ValueError("Venue ID already exists.")

            # Create a Venue object
            venue = Venue(*values)
            self.venues.append(venue)
            self.display_venues()
            self.clear_entries(entries)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to delete a venue
    def delete_venue(self):
        try:
            selected_item = self.venue_table.selection()
            if not selected_item:
                raise ValueError("Please select a venue to delete.")

            item = self.venue_table.item(selected_item)
            venue_id = item['values'][0]
            for venue in self.venues:
                if venue.venueId == venue_id:
                    self.venues.remove(venue)
                    break
            self.display_venues()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to create a window for modifying venue details
    def modify_venue_window(self):
        try:
            selected_item = self.venue_table.selection()
            if not selected_item:
                raise ValueError("Please select a venue to modify.")

            item = self.venue_table.item(selected_item)
            venue_id = item['values'][0]
            for venue in self.venues:
                if venue.venueId == venue_id:
                    modify_window = tk.Toplevel()
                    modify_window.title("Modify Venue")

                    # Labels and entry fields pre-filled with existing venue details
                    labels = ['Venue ID', 'Name', 'Address', 'Contact', 'Min Guests', 'Max Guests']
                    entries = []

                    for i, label in enumerate(labels):
                        tk.Label(modify_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        entry = tk.Entry(modify_window)
                        entry.grid(row=i, column=1, padx=5, pady=5)
                        entry.insert(tk.END, getattr(venue, label.lower()))
                        entries.append(entry)

                    # Button to modify the venue
                    modify_button = tk.Button(modify_window, text="Modify", command=lambda: self.modify_venue(venue, entries, modify_window))
                    modify_button.grid(row=len(labels), column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to modify venue details
    def modify_venue(self, venue, entries, modify_window):
        try:
            values = [entry.get() for entry in entries]
            if not values[0]:
                raise ValueError("Venue ID is a required field.")

            for v in self.venues:
                if v.venueId == values[0] and v != venue:
                    raise ValueError("Venue ID already exists.")

            # Update the Venue object
            venue.venueId = values[0]
            venue.name = values[1]
            venue.address = values[2]
            venue.contact = values[3]
            venue.minGuests = values[4]
            venue.maxGuests = values[5]

            self.display_venues()
            modify_window.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display details of a selected venue
    def display_venue_details(self):
        try:
            selected_item = self.venue_table.selection()
            if not selected_item:
                raise ValueError("Please select a venue to display details.")

            item = self.venue_table.item(selected_item)
            venue_id = item['values'][0]
            for venue in self.venues:
                if venue.venueId == venue_id:
                    details_window = tk.Toplevel()
                    details_window.title("Venue Details")

                    # Display venue details
                    labels = ['Venue ID', 'Name', 'Address', 'Contact', 'Min Guests', 'Max Guests']
                    for i, label in enumerate(labels):
                        tk.Label(details_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        tk.Label(details_window, text=getattr(venue, label.lower())).grid(row=i, column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display all venues in the table
    def display_venues(self):
        # Clear the table
        for item in self.venue_table.get_children():
            self.venue_table.delete(item)

        # Insert venues into the table
        for venue in self.venues:
            self.venue_table.insert('', 'end', values=(
                venue.venueId, venue.name, venue.address, venue.contact, venue.minGuests, venue.maxGuests))

    # Function to clear entry fields
    def clear_entries(self, entries):
        for entry in entries:
            entry.delete(0, tk.END)

# Run the Venue Manager GUI
VenueManagerGUI()
