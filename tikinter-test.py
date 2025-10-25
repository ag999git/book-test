######## NEXT ###########

######## NEXT ###########
#To create a simple Tkinter Python app, follow these basic steps
# Step 1: Import the Tkinter module
from tkinter import *
print("Tkinter module imported successfully.")
# Step 2: Create the main application window
root = Tk()
print("Main application window created.")
# Step 3: Use .title() to set the title of the window
root.title("My Tkinter Application")
print("Window title set to 'My Tkinter Application'.")
# Step 4: Create a widget of type Label
label = Label(root, text="Hello World")
print("Label widget created with text 'Hello, World'.")
# Step 5: Use .pack() to place the Label widget in the window
label.pack()
print("Label widget packed into the window.")
# Step 6: Start the Tkinter event loop
root.mainloop()
print("Tkinter event loop exited.")


######## NEXT ###########
# Write a small example script which shows the use of common Window Management Commands.
import tkinter as tk

# 1 Create the main window (root window)
root = tk.Tk() # Every Tkinter app must have one root window

# 2️ Set the window title
root.title("My App")

# 3️ Set the window size (width x height)
root.geometry("400x300")  # 400 pixels wide, 300 pixels tall

# 4️ Disable window resizing (width=False, height=False)
root.resizable(False, False)

# 5️ Set a custom window icon (optional)
# Make sure "app.ico" exists in your project folder.
# Comment out this line if you don’t have an icon file.
# root.iconbitmap("app.ico")

# 6️ Create a simple label widget inside the window
label = tk.Label(root, text="Welcome to my Tkinter window!", font=("Arial", 14))
label.pack(pady = 20)

# 7️ Add a button to close the window
def close_window():
    root.destroy()   # Closes the main window

# 8️ Create and pack the button
button = tk.Button(root, text="Close", command=close_window)
button.pack(pady=10)

# 9️ Start the event loop — this keeps the window running and responsive
root.mainloop()





######## NEXT ###########
# Write a Python Script which uses the Widget Creation Commands
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Widget Examples")
root.geometry("500x600")

# 1️ Label – displays text or image
lbl = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
lbl.pack(pady=10)

# 2️ Button – a clickable button
def on_button_click():
    lbl.config(text="Button was clicked!")

btn = tk.Button(root, text="Click Me", command=on_button_click)
btn.pack(pady=10)

# 3️ Entry – single-line text input
ent = tk.Entry(root, width=30)
ent.insert(0, "Type something here...")
ent.pack(pady=10)

# 4️ Text – multi-line text box
txt = tk.Text(root, height=4, width=40)
txt.insert(tk.END, "This is a multi-line Text widget.\nYou can write here.")
txt.pack(pady=10)

# 5️ Checkbutton – a checkbox
chk_var = tk.BooleanVar()
chk = tk.Checkbutton(root, text="I accept the terms", variable=chk_var)
chk.pack(pady=10)

# 6️ Radiobutton – radio button for options
rad_var = tk.StringVar(value="Option 1")
rad1 = tk.Radiobutton(root, text="Option 1", variable=rad_var, value="Option 1")
rad2 = tk.Radiobutton(root, text="Option 2", variable=rad_var, value="Option 2")
rad1.pack()
rad2.pack(pady=5)

# 7️ Listbox – list of items
lst = tk.Listbox(root, height=5)
for item in ["Python", "Java", "C++", "JavaScript", "Swift"]:
    lst.insert(tk.END, item)
lst.pack(pady=10)

# 8️ Canvas – drawing area for shapes or images
cv = tk.Canvas(root, width=200, height=100, bg="lightblue")
cv.create_oval(20, 20, 80, 80, fill="red")  # draw a circle
cv.create_text(100, 50, text="Canvas", font=("Arial", 10))
cv.pack(pady=10)

# 9️ Frame – container for grouping widgets
frm = tk.Frame(root, bd=2, relief="solid")
frm.pack(pady=10)

tk.Label(frm, text="Inside Frame").pack(padx=10, pady=5)
tk.Button(frm, text="Frame Button").pack(padx=10, pady=5)

# 10 Scrollbar – adds scrolling to text or listbox
scroll_frame = tk.Frame(root)
scroll_frame.pack(pady=10)

scrollbar = tk.Scrollbar(scroll_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

scroll_text = tk.Text(scroll_frame, height=4, width=40, yscrollcommand=scrollbar.set)
scroll_text.pack(side=tk.LEFT)
scrollbar.config(command=scroll_text.yview)

scroll_text.insert(tk.END, "This Text widget has a Scrollbar.\n" * 10)

# Start the event loop
root.mainloop()
# Following line will not be executed until the window is closed
print("Tkinter event loop ended.")

######## NEXT ###########
# Write a short script which explains the use of Widget Placement Commands of the Tkinter Python library
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

######## NEXT ###########
# 2.19 Write a small script which gives common Configuration and Properties of the Tkinter library.
import tkinter as tk

root = tk.Tk()
root.title("Configuration Example")
root.geometry("300x150")

# Create a Label
lbl = tk.Label(root, text="Original Text", fg="blue")
lbl.pack(pady=10)

# Function1 to update text using config()
def update_text():
    lbl.config(text="Updated using config()") # Change label text

# Function2 to get current text using cget()
def show_text():
    current = lbl.cget("text") # Get 'text' property
    lbl.config(text=f"Current: {current}")

# Function3 to change color using ['property'] = value
def change_color():
    lbl["fg"] = "red"  # Alternate way to set property
    lbl["text"] = "Color changed using ['fg']"

# Call to update_text() functions
tk.Button(root, text="Update Text", 
          command=update_text).pack(pady=3)
# Call to show_text function
tk.Button(root, text="Show Current Text", 
          command=show_text).pack(pady=3)
# Call to change_color() function
tk.Button(root, text="Change Color", 
          command=change_color).pack(pady=3)

root.mainloop()

######## NEXT ###########
# Write a small script which shows the use of Dialog and message commands in Tkinter Python.
import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser, simpledialog

root = tk.Tk()
root.title("Dialog Box Examples")
root.geometry("300x200")

# Function to show info message box
def show_info():
    messagebox.showinfo("Information", "This is an info popup!")

# Function to open file dialog
def open_file():
    filename = filedialog.askopenfilename(title="Select a file")
    if filename:
        messagebox.showinfo("Selected File", f"You chose:\n{filename}")

# Function to open color chooser
def choose_color():
    color = colorchooser.askcolor(title="Pick a color")
    if color[1]:
        messagebox.showinfo("Chosen Color", f"Hex code: {color[1]}")

# Function to open simple text input dialog
def ask_name():
    name = simpledialog.askstring("Input", "Enter your name:")
    if name:
        messagebox.showinfo("Hello", f"Hi {name}!")

# Create buttons to trigger each dialog
tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
tk.Button(root, text="Open File", command=open_file).pack(pady=5)
tk.Button(root, text="Choose Color", command=choose_color).pack(pady=5)
tk.Button(root, text="Ask Name", command=ask_name).pack(pady=5)

root.mainloop()

######## NEXT ###########
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("after() and after_cancel() Example")
root.geometry("300x200")

# Label to display messages
lbl = tk.Label(root, text="Click 'Start Timer' to begin", font=("Arial", 12))
lbl.pack(pady=20)

# Function to update label text after delay
def update_label():
    lbl.config(text="Updated after 2 seconds!")

# Function to start timer
def start_timer():
    global task_id  # make variable accessible outside function
    lbl.config(text="Timer started... will update soon")
    # Schedule update_label() to run after 2000 milliseconds (2 seconds)
    task_id = root.after(2000, update_label)

# Function to cancel scheduled task
def cancel_timer():
    if 'task_id' in globals():  # check if task was started
        root.after_cancel(task_id)
        lbl.config(text="Update cancelled!")

# Buttons for starting and cancelling timer
tk.Button(root, text="Start Timer", command=start_timer).pack(pady=5)
tk.Button(root, text="Cancel Timer", command=cancel_timer).pack(pady=5)

# Run Tkinter main loop
root.mainloop()

######## NEXT ###########

import tkinter as tk
from tkinter import ttk, messagebox

# Create main window
root = tk.Tk()
root.title("Simple ttk Example")
root.geometry("300x200")

# Function to handle button click (using command=)
def show_message():
    name = entry.get()  # get text from Entry
    messagebox.showinfo("Hello", f"Welcome, {name}!")  # show info dialog

# Label widget (ttk version)
lbl = ttk.Label(root, text="Enter your name:")
lbl.pack(pady=10)

# Entry widget to take input
entry = ttk.Entry(root)
entry.pack(pady=5)

# Button widget to show message
btn = ttk.Button(root, text="Say Hello", command=show_message)
btn.pack(pady=10)

# Function to handle mouse click event (using bind)
def on_click(event):
    messagebox.showinfo("Clicked", "You clicked inside the window!")

# Bind left mouse button click to the window
root.bind("<Button-1>", on_click)

# Run the Tkinter main loop
root.mainloop()



######## NEXT ###########


