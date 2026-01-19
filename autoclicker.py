import tkinter as tk
from tkinter import messagebox
import mouse
import keyboard
running = False
delay = 0

def start_clicker():
    global running, delay
    
    try:
        clicks_per_second = int(entry.get())
        
        
        
        if clicks_per_second <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive integer for clicks per second.")
            return
        

        delay = int(1000 / clicks_per_second)

        messagebox.showinfo("Auto Clicker", "Auto Clicker розпочато! Натисніть 'ESC', щоб зупинити.")
        running = True


        schedule_click()

    except ValueError:
        messagebox.showerror("Помилка вводу", "Будь ласка, введіть коректне число кліків на секунду.")

def schedule_click():

    if running:
        mouse.click()


        root.after(delay, schedule_click)

def exit_app():

    global running

    if running:

        running = False

    messagebox. showinfo("Auto Clicker", "Auto Clicker зупинено.")
    root.destroy()

def show_info(event):

    messagebox. showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

root = tk. Tk()
root. title("Auto Clicker")
root.geometry("300x220")
root.resizable(False, False)
root.configure(bg="#e0f7fa")


root.bind('i', show_info)

title_label = tk. Label(
    root,
    text="Auto Clicker",
    font=("Trebuchet MS", 16, "bold"),
    bg="#e0f7fa",
    fg="#00796b"
)
title_label.pack(pady=10)


label = tk. Label(
    root,
    text="Введіть кількість кліків на секунду:",
    font=("Trebuchet MS", 12),
    bg="#e0f7fa",
    fg="#00796b"
)
label.pack(pady=5)

# Entry for clicks per second
entry = tk.Entry(
    root,
    font=("Trebuchet MS", 12),
    width=10,
    justify=tk.CENTER
)
entry.insert(0, "10")
entry.pack(pady=5)
button_frame = tk. Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30))


start_button = tk. Button(
    button_frame,
    text="Розпочати",
    command=start_clicker,
    bg="#4caf50",
    activebackground="#66bb6a",
    fg="white",
    font=("Trebuchet MS", 12),
    width=12
)
start_button.grid(row=0, column=0, padx=10)


exit_button = tk. Button(
    button_frame,
    text="Зупинити",
    command=exit_app,
    bg="#f44336",
    activebackground="#e57373",
    fg="white",
    font=("Trebuchet MS", 12),
    width=8
)





keyboard. add_hotkey('esc', exit_app)


root.protocol("WM_DELETE_WINDOW", exit_app)


root.mainloop()