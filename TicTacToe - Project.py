import tkinter as tk
from tkinter import messagebox, Menu  # Import messagebox for error handling

window = tk.Tk()
window.geometry("500x500")
window.title("Tic Tac Toe")

clicked = True
count = 0
winner = False

# Define the buttons globally
b1 = None
b2 = None
b3 = None
b4 = None
b5 = None
b6 = None
b7 = None
b8 = None
b9 = None



# Disable all buttons
def disable_all_buttons():
    b1.config(state="disabled") # type: ignore
    b2.config(state="disabled") # type: ignore
    b3.config(state="disabled") # type: ignore
    b4.config(state="disabled")# type: ignore
    b5.config(state="disabled") # type: ignore
    b6.config(state="disabled")# type: ignore# type: ignore# type: ignore
    b7.config(state="disabled")# type: ignore
    b8.config(state="disabled")# type: ignore
    b9.config(state="disabled")# type: ignore

# Check if someone won
def checkifwon():
    global winner
    winner = False

    # Check for X wins
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":# type: ignore
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    # Check for O wins
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

# Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!")
        disable_all_buttons()

# Button click function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
    else:
        messagebox.showerror("Tic Tac Toe", "Hey pick another box!")

    checkifwon()

# Create a frame to hold buttons
frame = tk.Frame(window)
frame.pack(pady=20)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count, winner
    clicked = True
    count = 0
    winner = False

    # Reset button texts and backgrounds
    for button in (b1, b2, b3, b4, b5, b6, b7, b8, b9):
        button.config(text=" ", bg="Lightgray", state="normal")

# Button build
b1 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b1))
b2 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b2))
b3 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b3))

b4 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b4))
b5 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b5))
b6 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b6))

b7 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b7))
b8 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b8))
b9 = tk.Button(frame, text=" ", font=('Arial', 16), height=3, width=6, bg="Lightgray", command=lambda: b_click(b9))

# Grid of buttons
b1.grid(row=0, column=0, sticky="nsew")
b2.grid(row=0, column=1, sticky="nsew")
b3.grid(row=0, column =2, sticky = "nsew")
b4.grid(row=1, column=0, sticky="nsew")
b5.grid(row=1, column=1, sticky="nsew")
b6.grid(row=1, column=2, sticky="nsew")
b7.grid(row=2, column=0, sticky="nsew")
b8.grid(row=2, column=1, sticky="nsew")
b9.grid(row=2, column=2, sticky="nsew")

# Create menu
my_menu = Menu(window)
window.config(menu=my_menu)

# Create option menu 
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

window.mainloop()
