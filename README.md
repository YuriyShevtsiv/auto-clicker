

# 🖱 Auto Clicker (Tkinter)

## 📌 Description

<img width="309" height="248" alt="Screenshot 2026-04-11 104802" src="https://github.com/user-attachments/assets/19224b2e-279c-4ed6-80c6-282273f43e08" />
This project is a **simple Auto Clicker application** built with **Python and Tkinter**.
It allows the user to automatically click the mouse at a specified speed (clicks per second) using a graphical interface.

The application includes:

* Adjustable click speed
* Start and stop controls
* Global **ESC hotkey** to stop clicking
* Informational popups
* Ukrainian language interface

---

## 🛠 Requirements

* **Python 3.8+**
* Required Python libraries:

  * `tkinter` (included with Python)
  * `mouse`
  * `keyboard`

### Install required libraries:

```bash
pip install mouse keyboard
```

> ⚠️ **Note:**
> On some systems, the `mouse` and `keyboard` libraries may require **administrator/root privileges** to work correctly.

---

## ▶️ How to Run the Application

1. Save the code to a file, for example:

   ```bash
   auto_clicker.py
   ```

2. Run the application:

   ```bash
   python auto_clicker.py
   ```

3. The Auto Clicker window will appear.

---

## 🖥 Application Features

### 🔢 Click Speed Control

* Enter the number of **clicks per second** in the input field.
* Default value is `10`.

### ▶️ Start Button

* Click **"Розпочати"** to start the auto clicker.
* Mouse clicks will begin immediately.
* A message will confirm that the clicker has started.

### ⏹ Stop Button / ESC Key

* Click **"Зупинити"** to stop the auto clicker.
* Press **ESC** at any time to stop clicking and close the application.

### ℹ️ Info Shortcut

* Press the **`I` key** to display information about the application.

---

## ⚙️ How It Works

1. The user enters the desired number of clicks per second.
2. The program calculates the delay between clicks:

   ```
   delay = 1000 / clicks_per_second
   ```
3. The function `schedule_click()`:

   * Performs a mouse click
   * Reschedules itself using `root.after()`
4. Clicking stops when:

   * The **ESC** key is pressed
   * The **Stop** button is clicked
   * The window is closed

---

## 📂 Project Structure

```text
project-folder/
│
├── auto_clicker.py   # Main application file
└── README.md         # Documentation
```

---

## ⚠️ Important Notes

* This tool is intended **for educational purposes only**.
* Do not use auto clickers in games or services that prohibit automation.
* High click rates may affect system performance.

---

## 🧠 Learning Goals

This project helps you learn:

* Tkinter GUI development
* Event handling and hotkeys
* Working with external libraries
* Using `after()` for repeated actions
* Basic input validation and error handling

---

## 📄 License

This project is free to use for educational and personal learning purposes.
