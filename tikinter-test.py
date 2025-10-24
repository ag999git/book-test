

######## NEXT ###########
# 2. Write a short script which explains the use of Widget Placement Commands of the Tkinter Python library
import tkinter as tk

root = tk.Tk()
root.title("pack(), grid(), place() Example")
root.geometry("300x250")

# 1️ pack() — create and arrange main frames
top = tk.Frame(root, bg="lightblue", height=40)
top.pack(fill="x")

middle = tk.Frame(root, bg="lightyellow")
middle.pack(fill="both", expand=True)

bottom = tk.Frame(root, bg="lightgray", height=40)
bottom.pack(fill="x", side="bottom")

# 2️ grid() — arrange widgets in a table inside the middle frame
tk.Label(middle, text="Name:", bg="lightyellow").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(middle).grid(row=0, column=1, padx=5, pady=5)

tk.Label(middle, text="Age:", bg="lightyellow").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(middle).grid(row=1, column=1, padx=5, pady=5)

# 3️ place() — position buttons exactly inside the bottom frame
tk.Button(bottom, text="OK").place(x=80, y=5)
tk.Button(bottom, text="Cancel").place(x=160, y=5)

root.mainloop()

######## NEXT ###########
# Write a short simple script which shows the use of Event Handling and Commands
import tkinter as tk

root = tk.Tk()
root.title("Event Handling Example")
root.geometry("250x150")

# Define functions (handlers)
def on_click(event):      # Function for bind() event
    lbl.config(text="Button clicked using bind()")

def on_command():         # Function for command=
    lbl.config(text="Button clicked using command=")

# Label to display messages
lbl = tk.Label(root, text="Click a button")
lbl.pack(pady=10)

# Button 1 – uses bind()
btn1 = tk.Button(root, text="Bind Button")
btn1.pack(pady=5)
btn1.bind("<Button-1>", on_click)   # Left mouse click triggers on_click()

# Button 2 – uses command=
btn2 = tk.Button(root, text="Command Button", command=on_command)
btn2.pack(pady=5)

root.mainloop()
