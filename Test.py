import tkinter as tk

def main():
    screen = tk.Tk()
    label = tk.Label(screen, text = "Welcome to Expenses Tracker!")
    button = tk.Button(screen, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground = "", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

    button.pack(padx=20, pady=20)
    label.pack()
    screen.mainloop()

def button_clicked():
    print("Button was pressed.")

main()