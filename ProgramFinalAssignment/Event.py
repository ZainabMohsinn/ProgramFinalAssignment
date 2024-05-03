import tkinter as tk
from tkinter import ttk, messagebox

# Define a class for managing events
class Event:
    def __init__(self, eventId="", eventType="", theme="", date="", time="", duration="", venueAddress="", clientId="", guestList="", cateringCompany="", cleaningCompany="", decorationsCompany="", entertainmentCompany="", furnitureSupplyCompany="", invoice=""):
        self.__eventId = eventId
        self.__eventType = eventType
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venueAddress = venueAddress
        self.__clientId = clientId
        self.__guestList = guestList
        self.__cateringCompany = cateringCompany
        self.__cleaningCompany = cleaningCompany
        self.__decorationsCompany = decorationsCompany
        self.__entertainmentCompany = entertainmentCompany
        self.__furnitureSupplyCompany = furnitureSupplyCompany
        self.__invoice = invoice

    # Implement getters and setters for all attributes

# Define the GUI for managing events
class EventManagerGUI:
    def __init__(self):
        self.events = []  # List to store events
        self.root = tk.Tk()
        self.root.title("Event Manager")

        # Create a table to display event information
        self.table = ttk.Treeview(self.root, columns=('Event ID', 'Event Type', 'Theme', 'Date', 'Time', 'Duration'))
        self.table.heading('Event ID', text='Event ID')
        self.table.heading('Event Type', text='Event Type')
        self.table.heading('Theme', text='Theme')
        self.table.heading('Date', text='Date')
        self.table.heading('Time', text='Time')
        self.table.heading('Duration', text='Duration')
        self.table.pack(padx=10, pady=10)

        # Buttons for various operations
        self.add_button = tk.Button(self.root, text="Add Event", command=self.add_event_window)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Event", command=self.delete_event)
        self.delete_button.pack(pady=5)

        self.modify_button = tk.Button(self.root, text="Modify Event", command=self.modify_event_window)
        self.modify_button.pack(pady=5)

        self.display_button = tk.Button(self.root, text="Display Event Details", command=self.display_event_details)
        self.display_button.pack(pady=5)

        # Display existing events
        self.display_events()

        self.root.mainloop()

    # Function to create a window for adding a new event
    def add_event_window(self):
        add_window = tk.Toplevel()
        add_window.title("Add Event")

        # Labels and entry fields for event details
        labels = ['Event ID', 'Event Type', 'Theme', 'Date', 'Time', 'Duration', 'Venue Address', 'Client ID', 'Guest List', 'Catering Company', 'Cleaning Company', 'Decorations Company', 'Entertainment Company', 'Furniture Supply Company', 'Invoice']
        entries = []

        for i, label in enumerate(labels):
            tk.Label(add_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        # Button to add the event
        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_event(entries))
        add_button.grid(row=len(labels), column=1, padx=5, pady=5)

    # Function to add a new event
    def add_event(self, entries):
        try:
            values = [entry.get() for entry in entries]
            # Validate required fields
            if not values[0]:
                raise ValueError("Event ID is a required field.")

            for event in self.events:
                if event.getEventId() == values[0]:
                    raise ValueError("Event ID already exists.")

            # Create an Event object
            event = Event(*values)
            self.events.append(event)
            self.display_events()
            self.clear_entries(entries)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to clear entry fields
    def clear_entries(self, entries):
        for entry in entries:
            entry.delete(0, tk.END)

    # Function to delete an event
    def delete_event(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select an event to delete.")

            item = self.table.item(selected_item)
            event_id = item['values'][0]
            for event in self.events:
                if event.getEventId() == event_id:
                    self.events.remove(event)
                    break
            self.display_events()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to create a window for modifying event details
    def modify_event_window(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select an event to modify.")

            item = self.table.item(selected_item)
            event_id = item['values'][0]
            for event in self.events:
                if event.getEventId() == event_id:
                    modify_window = tk.Toplevel()
                    modify_window.title("Modify Event")

                    # Labels and entry fields pre-filled with existing event details
                    labels = ['Event ID', 'Event Type', 'Theme', 'Date', 'Time', 'Duration', 'Venue Address', 'Client ID', 'Guest List', 'Catering Company', 'Cleaning Company', 'Decorations Company', 'Entertainment Company', 'Furniture Supply Company', 'Invoice']
                    entries = []

                    for i, label in enumerate(labels):
                        tk.Label(modify_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        entry = tk.Entry(modify_window)
                        entry.grid(row=i, column=1, padx=5, pady=5)
                        entry.insert(tk.END, event.__dict__[label.lower().replace(' ', '')])
                        entries.append(entry)

                    # Button to modify the event
                    modify_button = tk.Button(modify_window, text="Modify", command=lambda: self.modify_event(event, entries, modify_window))
                    modify_button.grid(row=len(labels), column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to modify event details
    def modify_event(self, event, entries, modify_window):
        try:
            values = [entry.get() for entry in entries]
            if not values[0]:
                raise ValueError("Event ID is a required field.")

            for e in self.events:
                if e.getEventId() == values[0] and e != event:
                    raise ValueError("Event ID already exists.")

            # Update the Event object
            event.setEventId(values[0])
            event.setEventType(values[1])
            event.setTheme(values[2])
            event.setDate(values[3])
            event.setTime(values[4])
            event.setDuration(values[5])
            event.setVenueAddress(values[6])
            event.setClientId(values[7])
            event.setGuestList(values[8])
            event.setCateringCompany(values[9])
            event.setCleaningCompany(values[10])
            event.setDecorationsCompany(values[11])
            event.setEntertainmentCompany(values[12])
            event.setFurnitureSupplyCompany(values[13])
            event.setInvoice(values[14])

            self.display_events()
            modify_window.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display details of a selected event
    def display_event_details(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select an event to display details.")

            item = self.table.item(selected_item)
            event_id = item['values'][0]
            for event in self.events:
                if event.getEventId() == event_id:
                    details_window = tk.Toplevel()
                    details_window.title("Event Details")

                    # Display event details
                    labels = ['Event ID', 'Event Type', 'Theme', 'Date', 'Time', 'Duration', 'Venue Address', 'Client ID', 'Guest List', 'Catering Company', 'Cleaning Company', 'Decorations Company', 'Entertainment Company', 'Furniture Supply Company', 'Invoice']
                    for i, label in enumerate(labels):
                        tk.Label(details_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        tk.Label(details_window, text=event.__dict__[label.lower().replace(' ', '')]).grid(row=i, column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display all events in the table
    def display_events(self):
        # Clear the table
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert events into the table
        for event in self.events:
            self.table.insert('', 'end', values=(
                event.getEventId(), event.getEventType(), event.getTheme(), event.getDate(), event.getTime(), event.getDuration()))

# Run the GUI
EventManagerGUI()
