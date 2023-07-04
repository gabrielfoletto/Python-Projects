import tkinter as tk 

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        root.configure(bg="#292b2f")    
        # Create the display
        self.display = tk.Entry(root, width=40, borderwidth=10) 
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=20)
        self.display.configure(font=("Arial", 8))
        # Create the buttons
        self.button1 = tk.Button(root, text="1", padx=20, pady=5, command=lambda: self.add_to_display("1"))
        self.button2 = tk.Button(root, text="2", padx=20, pady=5, command=lambda: self.add_to_display("2"))
        self.button3 = tk.Button(root, text="3", padx=20, pady=5, command=lambda: self.add_to_display("3"))
        self.button4 = tk.Button(root, text="4", padx=20, pady=5, command=lambda: self.add_to_display("4"))
        self.button5 = tk.Button(root, text="5", padx=20, pady=5, command=lambda: self.add_to_display("5"))
        self.button6 = tk.Button(root, text="6", padx=20, pady=5, command=lambda: self.add_to_display("6"))
        self.button7 = tk.Button(root, text="7", padx=20, pady=5, command=lambda: self.add_to_display("7"))
        self.button8 = tk.Button(root, text="8", padx=20, pady=5, command=lambda: self.add_to_display("8"))
        self.button9 = tk.Button(root, text="9", padx=20, pady=5, command=lambda: self.add_to_display("9"))
        self.button0 = tk.Button(root, text="0", padx=20, pady=5, command=lambda: self.add_to_display("0"))
        self.button_decimal = tk.Button(root, text=".", padx=21, pady=5, command=lambda: self.add_to_display("."))
        self.button_add = tk.Button(root, text="+", padx=19, pady=5, command=lambda: self.add_to_display("+"))
        self.button_sub = tk.Button(root, text="-", padx=20, pady=5, command=lambda: self.add_to_display("-"))
        self.button_multi = tk.Button(root, text="X", padx=19, pady=5, command=lambda: self.add_to_display("*"))
        self.button_div = tk.Button(root, text="/", padx=20, pady=5, command=lambda: self.add_to_display("/"))
        self.button_per = tk.Button(root, text="%", padx=18, pady=5, command=self.calculate_percentage)
        self.button_equal = tk.Button(root, text="=", padx=20, pady=5, command=self.calculate)
        self.button_clear = tk.Button(root, text="C", padx=20, pady=5, command=self.clear_display)
        self.button1.grid(row=3, column=0)
        self.button1.configure(bg="black", fg="yellow")
        self.button2.grid(row=3, column=1)
        self.button2.configure(bg="black", fg="yellow")
        self.button3.grid(row=3, column=2)
        self.button3.configure(bg="black", fg="yellow")
        self.button4.grid(row=2, column=0)
        self.button4.configure(bg="black", fg="yellow")
        self.button5.grid(row=2, column=1)
        self.button5.configure(bg="black", fg="yellow")
        self.button6.grid(row=2, column=2)
        self.button6.configure(bg="black", fg="yellow")
        self.button7.grid(row=1, column=0)
        self.button7.configure(bg="black", fg="yellow")
        self.button8.grid(row=1, column=1)
        self.button8.configure(bg="black", fg="yellow")
        self.button9.grid(row=1, column=2)
        self.button9.configure(bg="black", fg="yellow")
        self.button0.grid(row=4, column=1)
        self.button0.configure(bg="black", fg="yellow")
        self.button_decimal.grid(row=4, column=0)
        self.button_decimal.configure(bg="black", fg="yellow")
        self.button_add.grid(row=1, column=3)
        self.button_add.configure(bg="yellow", fg="black")
        self.button_sub.grid(row=2, column=3)
        self.button_sub.configure(bg="yellow", fg="black")
        self.button_multi.grid(row=3, column=3)
        self.button_multi.configure(bg="yellow", fg="black")
        self.button_per.grid(row=4, column=2)
        self.button_per.configure(bg="yellow", fg="black")
        self.button_div.grid(row=4, column=3)
        self.button_div.configure(bg="yellow", fg="black")
        self.button_equal.grid(row=1, column=4)
        self.button_equal.configure(bg="black", fg="yellow")
        self.button_clear.grid(row=2, column=4)
        self.button_clear.configure(bg="#695f20", fg="black")

    # functions
    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def calculate_percentage(self):
        current_value = self.display.get()
        if current_value.isdigit():
            current_value = int(current_value)
            per = current_value / 100
            self.display.delete(0, tk.END)
            self.display.insert(0, per)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def add_to_display(self, text):
        self.display.insert(tk.END, text)
        self.button1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: self.add_to_display("1"))

    def clear_display(self):
        self.display.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()