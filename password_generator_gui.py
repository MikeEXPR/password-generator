import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_slider.get())
    use_uppercase = var_uppercase.get()
    use_lowercase = var_lowercase.get()
    use_numbers = var_numbers.get()
    use_special = var_special.get()

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character set!")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    output_entry.delete(0, tk.END)
    output_entry.insert(0, password)

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Random Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Password Length
tk.Label(root, text="Select Password Length:").pack()
length_slider = tk.Scale(root, from_=4, to=32, orient="horizontal")
length_slider.set(12)
length_slider.pack(pady=5)

# Checkboxes for character options
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).pack(anchor="w", padx=20)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Output Field
output_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
output_entry.pack(pady=10, fill="x", padx=20)

# Run the App
root.mainloop()