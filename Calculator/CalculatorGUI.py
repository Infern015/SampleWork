import tkinter as tk
import math

# === Initialize ===
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False, False)

# === State ===
expression = ""
history = []
dark_mode = False
sci_mode = False

# === Theme Colors ===
light_theme = {"bg": "white", "fg": "black", "btn_bg": "lightgrey"}
dark_theme = {"bg": "#2b2b2b", "fg": "white", "btn_bg": "#444"}
current_theme = light_theme

# === Entry ===
equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=("Arial", 24), bd=10, relief="sunken", justify="right")
entry.pack(fill="both", ipadx=8, ipady=10)

# === History ===
history_label = tk.Label(root, text="History", font=("Arial", 12, "bold"))
history_label.pack()
history_box = tk.Listbox(root, height=4)
history_box.pack(fill="x")

# === Update Theme ===
def update_theme():
    theme = dark_theme if dark_mode else light_theme
    root.configure(bg=theme["bg"])
    entry.configure(bg=theme["bg"], fg=theme["fg"], insertbackground=theme["fg"])
    history_box.configure(bg=theme["bg"], fg=theme["fg"])
    for b in buttons_list + sci_buttons:
        b.configure(bg=theme["btn_bg"], fg=theme["fg"])

# === Expression Logic ===
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def equal_press():
    global expression
    try:
        result = str(eval(expression))
        history.append(expression + " = " + result)
        update_history()
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def scientific(func):
    global expression
    try:
        value = str(eval(expression))
        result = str(getattr(math, func)(float(value)))
        history.append(f"{func}({value}) = {result}")
        update_history()
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def update_history():
    history_box.delete(0, tk.END)
    for item in history[-5:]:
        history_box.insert(tk.END, item)

# === Toggle Dark Mode ===
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_theme()

# === Toggle Scientific Mode ===
def toggle_sci_mode():
    global sci_mode
    sci_mode = not sci_mode
    for b in sci_buttons:
        b.pack(side="left", expand=True, fill="both", padx=1, pady=1) if sci_mode else b.pack_forget()

# === Buttons ===
buttons_frame = tk.Frame(root)
buttons_frame.pack(fill="both", expand=True)

standard_buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
]

buttons_list = []
for row in standard_buttons:
    row_frame = tk.Frame(buttons_frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        cmd = (
            toggle_dark_mode if char == 'Dark' else
            toggle_sci_mode if char == 'Sci' else
            equal_press if char == '=' else
            clear if char == 'C' else
            lambda c=char: press(c)
        )
        btn = tk.Button(row_frame, text=char, font=("Arial", 16), command=cmd)
        btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)
        buttons_list.append(btn)

# === Scientific Buttons (Initially Hidden) ===
sci_row = tk.Frame(buttons_frame)
sci_row.pack(expand=True, fill="both")
sci_buttons = []

for func in ['sin', 'cos', 'tan', 'log', 'sqrt', 'exp']:
    btn = tk.Button(sci_row, text=func, font=("Arial", 16), command=lambda f=func: scientific(f))
    sci_buttons.append(btn)
    btn.pack_forget()

# === Mode Toggle Row ===
mode_row = tk.Frame(root)
mode_row.pack(fill="x", pady=5)

tk.Button(mode_row, text="Dark Mode", font=("Arial", 12), command=toggle_dark_mode).pack(side="left", expand=True, fill="x")
tk.Button(mode_row, text="Scientific Mode", font=("Arial", 12), command=toggle_sci_mode).pack(side="right", expand=True, fill="x")

# === Keyboard Support ===
def key_event(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        press(key)
    elif key == "\r":
        equal_press()
    elif key == "\x08":
        clear()

root.bind("<Key>", key_event)

update_theme()
root.mainloop()
