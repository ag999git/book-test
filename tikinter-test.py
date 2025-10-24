



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
