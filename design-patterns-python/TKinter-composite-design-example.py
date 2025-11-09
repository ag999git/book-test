


# ---------- Composite Design Pattern in Tkinter ----------
# Real-world example using Python's built-in Tkinter GUI library.

import tkinter as tk

# ---------- Leaf Components ----------
class LabelWidget:
    """Leaf: Can only display text."""
    def __init__(self, master, text):
        self.widget = tk.Label(master, text=text)

    def render(self):
        self.widget.pack()

class ButtonWidget:
    """Leaf: A clickable button."""
    def __init__(self, master, text):
        self.widget = tk.Button(master, text=text)

    def render(self):
        self.widget.pack()

# ---------- Composite Component ----------
class Window:
    """Composite: Can contain many widgets (leaves)."""
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.children = []  # Holds all leaf widgets

    def add(self, component):
        """Add a Label or Button to the window."""
        self.children.append(component)

    def render(self):
        """Render all child components."""
        for child in self.children:
            child.render()
        self.root.mainloop()


# ---------- Usage ----------
# Create main window (Composite)
window = Window("Composite Pattern Demo")

# Add leaves (simple widgets)
window.add(LabelWidget(window.root, "Welcome to the App"))
window.add(ButtonWidget(window.root, "OK"))
window.add(ButtonWidget(window.root, "Cancel"))

# Render everything together
window.render()
