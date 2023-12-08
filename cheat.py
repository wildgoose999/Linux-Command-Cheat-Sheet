import tkinter as tk
import pyperclip

def add_command():
    command = command_entry.get()
    if command:
        commands_listbox.insert(tk.END, command)
        command_entry.delete(0, tk.END)
        save_commands()

def copy_command(event):
    selected = event.widget.curselection()
    if selected:
        command = event.widget.get(selected[0])
        pyperclip.copy(command)

def remove_command():
    selected = commands_listbox.curselection()
    if selected:
        commands_listbox.delete(selected[0])
        save_commands()

def load_commands():
    try:
        with open("commands.txt", "r") as file:
            for command in file:
                commands_listbox.insert(tk.END, command.strip())
    except FileNotFoundError:
        pass

def save_commands():
    with open("commands.txt", "w") as file:
        for command in commands_listbox.get(0, tk.END):
            file.write(command + "\n")

# Create the main window
root = tk.Tk()
root.title("Linux Command Cheat Sheet")
root.geometry("400x500")
root.configure(bg='#2D2D2D')

# Command entry and add button
command_entry = tk.Entry(root, foreground="white", background="#808080")  # Grey background
command_entry.pack(pady=10)
add_button = tk.Button(root, text="Add Command", command=add_command, foreground="white", background="#3C3F41")
add_button.pack()

# Commands listbox
commands_listbox = tk.Listbox(root, foreground="white", background="#3C3F41")
commands_listbox.pack(expand=True, fill=tk.BOTH, pady=10)
commands_listbox.bind("<Double-1>", copy_command)

# Remove command button
remove_button = tk.Button(root, text="Remove Selected Command", command=remove_command, foreground="white", background="#3C3F41")
remove_button.pack(pady=5)

load_commands()

root.mainloop()
