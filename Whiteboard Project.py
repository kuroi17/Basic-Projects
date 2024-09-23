import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

# Initialize previous coordinates
prev_x, prev_y = None, None

def paint(event):
    global prev_x, prev_y
    if prev_x and prev_y:
        # Draw a line from the previous coordinates to the current coordinates
        canvas.create_line(prev_x, prev_y, event.x, event.y, fill=color.get(), width=scale.get())
    # Update previous coordinates
    prev_x, prev_y = event.x, event.y

def clear_canvas():
    global prev_x, prev_y
    canvas.delete('all')
    prev_x, prev_y = None, None

def change_color():
    new_color = askcolor(color=color.get())[1]
    if new_color:
        color.set(new_color)

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Whiteboard")

    canvas = tk.Canvas(window, bg='white', width=400, height=400)
    canvas.pack(fill='both', expand=True)
    canvas.bind('<B1-Motion>', paint)
    canvas.bind('<ButtonRelease-1>', lambda event: clear_previous_coords())

    def clear_previous_coords():
        global prev_x, prev_y
        prev_x, prev_y = None, None

    control_frame = ttk.Frame(window)
    control_frame.pack(side='bottom', fill='x')

    color_label = ttk.Label(control_frame, text='Color:', font=('Helvetica', 20))
    color_label.pack(side='left', padx=5, pady=5)

    color = tk.StringVar()
    color.set('black')
    color_button = tk.Button(control_frame, text='Choose Color', font=('Arial 10 bold'), bg='lightblue', command=change_color)
    color_button.pack(side='left', padx=5, pady=5)

    scale_label = ttk.Label(control_frame, text="Brush Size:", font=('Arial', 20))
    scale_label.pack(side='left', padx=5, pady=5)

    scale = tk.Scale(control_frame, from_=1, to=50, orient='horizontal', borderwidth=5, font=10)
    scale.pack(side='left', padx=5, pady=(5, 27))

    clear_button = tk.Button(control_frame, text='Clear', font=('Arial 10 bold'), bg='lightblue', command=clear_canvas)
    clear_button.pack(side='right', padx=5, pady=5)

    window.mainloop()


