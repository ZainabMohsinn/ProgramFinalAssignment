import tkinter as tk
from tkinter import ttk, messagebox

# Define a base class for a Person
class Person:
    def __init__(self, name=""):
        self.name = name

# Define a subclass Employee, inheriting from Person
class Employee(Person):
    def __init__(self, name="", id="", department="", jobTitle="", basicSalary="", age="", dateOfBirth="", passportDetails=""):
        super().__init__(name)
        self.id = id
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.age = age
        self.dateOfBirth = dateOfBirth
        self.passportDetails = passportDetails

# Define the GUI for managing employees
class EmployeeManagerGUI:
    def __init__(self):
        # Initialize list to store employee objects
        self.employees = []

        # Create main window
        self.root = tk.Tk()
        self.root.title("Employee Manager")

        # Create a table to display employee information
        self.table = ttk.Treeview(self.root, columns=(
        'Name', 'ID', 'Department', 'Job Title', 'Basic Salary', 'Age', 'Date of Birth', 'Passport Details'))
        self.table.heading('Name', text='Name')
        self.table.heading('ID', text='ID')
        self.table.heading('Department', text='Department')
        self.table.heading('Job Title', text='Job Title')
        self.table.heading('Basic Salary', text='Basic Salary')
        self.table.heading('Age', text='Age')
        self.table.heading('Date of Birth', text='Date of Birth')
        self.table.heading('Passport Details', text='Passport Details')
        self.table.pack(padx=10, pady=10)

        # Buttons for various operations
        self.add_button = tk.Button(self.root, text="Add Employee", command=self.add_employee_window)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Employee", command=self.delete_employee)
        self.delete_button.pack(pady=5)

        self.modify_button = tk.Button(self.root, text="Modify Employee", command=self.modify_employee_window)
        self.modify_button.pack(pady=5)

        self.display_button = tk.Button(self.root, text="Display Employee Details",
                                        command=self.display_employee_details)
        self.display_button.pack(pady=5)

        self.root.mainloop()

    # Function to create a window for adding a new employee
    def add_employee_window(self):
        add_window = tk.Toplevel()
        add_window.title("Add Employee")

        # Labels and entry fields for employee details
        labels = ['Name', 'ID', 'Department', 'Job Title', 'Basic Salary', 'Age', 'Date of Birth', 'Passport Details']
        entries = []

        for i, label in enumerate(labels):
            tk.Label(add_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        # Button to add the employee
        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_employee(entries))
        add_button.grid(row=len(labels), column=1, padx=5, pady=5)

    # Function to add a new employee
    def add_employee(self, entries):
        try:
            values = [entry.get() for entry in entries]
            if not values[0] or not values[1]:
                raise ValueError("Name and ID are required fields.")

            for employee in self.employees:
                if employee.id == values[1]:
                    raise ValueError("Employee ID already exists.")

            # Create new employee object and add to the list
            employee = Employee(name=values[0], id=values[1], department=values[2], jobTitle=values[3],
                                basicSalary=values[4], age=values[5], dateOfBirth=values[6], passportDetails=values[7])
            self.employees.append(employee)
            self.display_employees()
            self.clear_entries(entries)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to clear entry fields
    def clear_entries(self, entries):
        for entry in entries:
            entry.delete(0, tk.END)

    # Function to delete an employee
    def delete_employee(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select an employee to delete.")

            item = self.table.item(selected_item)
            employee_id = item['values'][1]
            for employee in self.employees:
                if employee.id == employee_id:
                    self.employees.remove(employee)
                    break
            self.display_employees()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to create a window for modifying employee details
    def modify_employee_window(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select an employee to modify.")

            item = self.table.item(selected_item)
            employee_id = item['values'][1]
            for employee in self.employees:
                if employee.id == employee_id:
                    modify_window = tk.Toplevel()
                    modify_window.title("Modify Employee")

                    # Labels and entry fields pre-filled with existing employee details
                    labels = ['Name', 'ID', 'Department', 'Job Title', 'Basic Salary', 'Age', 'Date of Birth',
                              'Passport Details']
                    entries = []

                    for i, label in enumerate(labels):
                        tk.Label(modify_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        entry = tk.Entry(modify_window)
                        entry.grid(row=i, column=1, padx=5, pady=5)
                        entry.insert(tk.END, employee.__dict__[label.lower().replace(' ', '')])
                        entries.append(entry)

                    # Button to modify the employee
                    modify_button = tk.Button(modify_window, text="Modify",
                                              command=lambda: self.modify_employee(employee, entries, modify_window))
                    modify_button.grid(row=len(labels), column=1, padx=5, pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to modify employee details
    def modify_employee(self, employee, entries, modify_window):
        try:
            values = [entry.get() for entry in entries]
            if not values[0] or not values[1]:
                raise ValueError("Name and ID are required fields.")

            for e in self.employees:
                if e.id == values[1] and e != employee:
                    raise ValueError("Employee ID already exists.")

            # Update employee details
            employee.name = values[0]
            employee.id = values[1]
            employee.department = values[2]
            employee.jobTitle = values[3]
            employee.basicSalary = values[4]
            employee.age = values[5]
            employee.dateOfBirth = values[6]
            employee.passportDetails = values[7]

            self.display_employees()
            modify_window.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display details of a selected employee
    def display_employee_details(self):
        try:
            selected_item = self.table.selection()
            if not selected_item:
                raise ValueError("Please select an employee to display details.")

            item = self.table.item(selected_item)
            employee_id = item['values'][1]
            for employee in self.employees:
                if employee.id == employee_id:
                    details_window = tk.Toplevel()
                    details_window.title("Employee Details")

                    # Display employee details
                    labels = ['Name', 'ID', 'Department', 'Job Title', 'Basic Salary', 'Age', 'Date of Birth',
                              'Passport Details']
                    for i, label in enumerate(labels):
                        tk.Label(details_window, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
                        tk.Label(details_window, text=employee.__dict__[label.lower().replace(' ', '')]).grid(row=i,
                                                                                                                column=1,
                                                                                                                padx=5,
                                                                                                                pady=5)
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Function to display all employees in the table
    def display_employees(self):
        # Clear the table
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert employees into the table
        for employee in self.employees:
            self.table.insert('', 'end', values=(
            employee.name, employee.id, employee.department, employee.jobTitle, employee.basicSalary, employee.age,
            employee.dateOfBirth, employee.passportDetails))

# Run the GUI
EmployeeManagerGUI()
