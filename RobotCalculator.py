import tkinter as tk
from tkinter import messagebox
from db import Database
from PIL import ImageTk, Image
import os
import Calculation

# Instanciate databse object
db = Database('store.db')

# Main Application/GUI class


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Robot Calculator - Beta (Stanley Black & Decker CoE)')
        # Width height
        master.geometry("700x400")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        # From Input
        self.from_text = tk.StringVar()
        self.from_label = tk.Label(
            self.master, text='From', font=('bold', 14), pady=20)
        self.from_label.grid(row=0, column=0, sticky=tk.W)
        self.from_entry = tk.Entry(self.master, textvariable=self.from_text)
        self.from_entry.grid(row=0, column=1)
        # To Input
        self.to_list = tk.StringVar()
        self.to_label = tk.Label(
            self.master, text='To', font=('bold', 14))
        self.to_label.grid(row=0, column=2, sticky=tk.W)
        self.to_entry = tk.Entry(
            self.master, textvariable=self.to_list)
        self.to_entry.grid(row=0, column=3)
        # ProductionRate
        self.ProductionRate = tk.StringVar()
        self.ProductionRate_label = tk.Label(
            self.master, text='Production Rate', font=('bold', 14))
        self.ProductionRate_label.grid(row=1, column=0, sticky=tk.W)
        self.ProductionRate_entry = tk.Entry(
            self.master, textvariable=self.ProductionRate)
        self.ProductionRate_entry.grid(row=1, column=1)
        # Distance
        self.Distance_text = tk.StringVar()
        self.Distance_label = tk.Label(
            self.master, text="Distance in 'm'", font=('bold', 14))
        self.Distance_label.grid(row=1, column=2, sticky=tk.W)
        self.Distance_entry = tk.Entry(self.master, textvariable=self.Distance_text)
        self.Distance_entry.grid(row=1, column=3)

        # From to list (listbox)
        self.from_to_list = tk.Listbox(self.master, height=8, width=50, border=0)
        self.from_to_list.grid(row=3, column=0, columnspan=3,
                             rowspan=6, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        # Set scrollbar to Trips
        self.from_to_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.from_to_list.yview)

        # Bind select
        self.from_to_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons
        self.add_btn = tk.Button(
            self.master, text="Add Trip", width=12, command=self.add_item)
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(
            self.master, text="Remove Trip", width=12, command=self.remove_item)
        self.remove_btn.grid(row=2, column=1)

        self.update_btn = tk.Button(
            self.master, text="Update Trip", width=12, command=self.update_item)
        self.update_btn.grid(row=2, column=2)

        self.exit_btn = tk.Button(
            self.master, text="Clear Input", width=12, command=self.clear_text)
        self.exit_btn.grid(row=2, column=3)

        self.calc_btn = tk.Button(
            self.master, text="Calculate", width=12, command=self.display_result)        
        self.calc_btn.grid(row=3, column=4)

    def populate_list(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.from_to_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetch():
            # Insert into list
            self.from_to_list.insert(tk.END, row)

    # Add new item
    def add_item(self):
        if self.from_text.get() == '' or self.to_list.get() == '' or self.ProductionRate.get() == '' or self.Distance_text.get() == '':
            messagebox.showerror("Required Fields", "Please include all fields")
            return
        print(self.from_text.get())
        # Insert into DB
        db.insert(self.from_text.get(), self.to_list.get(),
                  self.ProductionRate.get(), self.Distance_text.get())
        # Clear list
        self.from_to_list.delete(0, tk.END)
        # Insert into list
        self.from_to_list.insert(tk.END, (self.from_text.get(), self.to_list.get(
        ), self.ProductionRate.get(), self.Distance_text.get()))
        self.clear_text()
        self.populate_list()

    # Runs when item is selected
    def select_item(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.from_to_list.curselection()[0]
            # Get selected item
            self.selected_item = self.from_to_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            self.from_entry.delete(0, tk.END)
            self.from_entry.insert(tk.END, self.selected_item[1])
            self.to_entry.delete(0, tk.END)
            self.to_entry.insert(tk.END, self.selected_item[2])
            self.ProductionRate_entry.delete(0, tk.END)
            self.ProductionRate_entry.insert(tk.END, self.selected_item[3])
            self.Distance_entry.delete(0, tk.END)
            self.Distance_entry.insert(tk.END, self.selected_item[4])
        except IndexError:
            pass

    # Remove item
    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        db.update(self.selected_item[0], self.from_text.get(
        ), self.to_list.get(), self.ProductionRate.get(), self.Distance_text.get())
        self.populate_list()

    # Clear all text fields
    def clear_text(self):
        self.from_entry.delete(0, tk.END)
        self.to_entry.delete(0, tk.END)
        self.ProductionRate_entry.delete(0, tk.END)
        self.Distance_entry.delete(0, tk.END)

    def display_result(self):
        Calculation.calculate()
        tk.messagebox.showinfo(title='Result', message=f"You will need {Calculation.display_result()} to accommodate your request. To round up, you will need {Calculation.display_result_ru()}")

    
root = tk.Tk()
# img = ImageTk.PhotoImage(Image.open("Stanley_Black_&_Decker_logo.png"))
# panel = tk.Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
app = Application(master=root)
app.mainloop()