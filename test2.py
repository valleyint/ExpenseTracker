import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Simple Table with Tkinter")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Age", "City"), show='headings')

# Define the headings
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("City", text="City")

# Define the column widths
'''tree.column("Name", width=100)
tree.column("Age", width=50)
tree.column("City", width=100)'''

# Insert some sample data
data = [["salary1", "salary2", "salary3"], [100.0, 300.0, 500.0]]

for item in data[0]:
    tree.insert("", tk.END, values=item)
for item in data[1]:
    tree.insert("", tk.END ,column = 1, values=item)
# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')

# Pack the Treeview widget
tree.pack(side='left', fill='both', expand=True)

# Start the Tkinter event loop
root.mainloop()