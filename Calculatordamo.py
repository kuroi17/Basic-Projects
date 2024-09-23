import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current_text = textbox.get("1.0", tk.END).strip()
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, current_text + value)

# Function to clear the textbox
def clear_textbox():
    textbox.delete("1.0", tk.END)

# Function to calculate the result
def calculate_result():
    try:
       result = eval(textbox.get("1.0", tk.END).replace('×', '*').replace('÷', '/').strip())
       clear_textbox()
       textbox.insert(tk.END, str(result))
    except Exception:
        clear_textbox()
        textbox.insert(tk.END, "ERROR")
       # clear_textbox()
       # textbox.insert(tk.END, "i miss u balik ka na raw")

# Shape and title
window = tk.Tk()
window.geometry("300x360")
window.title("Calculator Sa Palengke")
window.configure(bg="forestgreen") # kulay for window

# Textbox
textbox = tk.Text(window, bg='lightsteelblue', height=2, font=('Arial', 18))
textbox.pack(padx=10, pady=10,fill="x")

# Button frame
buttonframe = tk.Frame(window, bg='forestgreen')
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("4", 1, 3),
    ("5", 2, 0), ("6", 2, 1), ("7", 2, 2), ("8", 2, 3),
    ("9", 3, 0), ("0", 3, 1), ("×", 3, 2), ("÷", 3, 3),
    ("+", 4, 0), ("-", 4, 1), (".", 4, 2), ("=", 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == "=":
        action = calculate_result
    else:
        action = lambda x=text: button_click(x)
   # color putting in arithmetic operation
    btn_orangeblue = {'text': text, 'font':('Arial',18),'command':action, 'bd':5} #cganges
    
    if text in {"×","÷", "+", "-", "=", ".", "C"}:
        btn_orangeblue['bg'] = 'olive'
    elif text in {"1","2","3","4","5","6","7","8","9","0"}:
     btn_orangeblue['bg'] = 'yellowgreen'
    btn = tk.Button(buttonframe, btn_orangeblue)
    btn.grid(row=row,column = col, sticky = tk.E + tk.W + tk.N + tk.S , padx=1.5, pady=1.5)#changes


# Add the clear button
    btn_clear = tk.Button(buttonframe, bg= 'olive' ,text="C", font=('Arial', 18), command=clear_textbox, fg = 'white' , bd= 5) #bd changes
btn_clear.grid(row=5, column=0, columnspan=4, sticky=tk.E + tk.W + tk.N + tk.S)

buttonframe.pack(fill='x', padx=1.5, pady=1.5) #changes
window.mainloop()