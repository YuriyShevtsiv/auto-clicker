import tkinter as tk
from tkinter import messagebox
import mouse
import keyboard

running = False
delay = 0


def start_clicker():
    global running, delay

    if running:
        return  # prevent multiple loops

    try:
        clicks_per_second = int(entry.get())

        if clicks_per_second <= 0:
            raise ValueError

        delay = int(1000 / clicks_per_second)
        running = True

        messagebox.showinfo(
            "Auto Clicker",
            "Auto Clicker розпочато!\nНатисніть ESC, щоб зупинити."
        )

        schedule_click()

    except ValueError:
        messagebox.showerror(
            "Помилка вводу",
            "Будь ласка, введіть додатне ціле число."
        )


def schedule_click():
    if running:
        mouse.click()
        root.after(delay, schedule_click)


def stop_clicker():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")


def exit_app():
    stop_clicker()
    root.destroy()


def show_info(event=None):
    messagebox.showinfo(
        "Інформація",
        "Це автоклікер. Він клікає мишкою зі швидкістю, яку ти вкажеш 😉"
    )


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x220")
root.resizable(False, False)
root.configure(bg="#e0f7fa")

root.bind('i', show_info)

title_label = tk.Label(
    root,
    text="Auto Clicker",
    font=("Trebuchet MS", 16, "bold"),
    bg="#e0f7fa",
    fg="#00796b"
)
title_label.pack(pady=10)

label = tk.Label(
    root,
    text="Введіть кількість кліків на секунду:",
    font=("Trebuchet MS", 12),
    bg="#e0f7fa",
    fg="#00796b"
)
label.pack(pady=5)

entry = tk.Entry(
    root,
    font=("Trebuchet MS", 12),
    width=10,
    justify=tk.CENTER
)
entry.insert(0, "10")
entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30))

start_button = tk.Button(
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

exit_button = tk.Button(
    button_frame,
    text="Зупинити",
    command=stop_clicker,
    bg="#f44336",
    activebackground="#e57373",
    fg="white",
    font=("Trebuchet MS", 12),
    width=8
)
exit_button.grid(row=0, column=1, padx=10)

keyboard.add_hotkey('esc', stop_clicker)
root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()