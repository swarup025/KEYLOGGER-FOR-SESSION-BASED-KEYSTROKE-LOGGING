# 🛡️ Python Keylogger with Session Tracking

A simple keystroke logger built using `pynput` in Python. This tool captures keyboard inputs and logs them into a file (`key_log.txt`). It also tracks session start times for better organization.

---

## ⚙️ Features

- Captures all keystrokes using the `pynput` library.
- Logs keys into a text file: `key_log.txt`.
- Tracks and labels new keyboard session starts.
- Stops logging when the **ESC key** is pressed.
- Lightweight and easy to use for educational purposes.

---

## 🛠️ Technologies Used

- Python 3.x
- `pynput` module (`pip install pynput`)

---

## 🚀 How It Works

1. When you run the script, a new session header is added to `key_log.txt`.
2. Each key you press is recorded and appended to the log.
3. Press the `ESC` key to stop the logger.

---

## 🧪 Sample Output (key_log.txt)

New session started
a
b
c
Key.space
d
Key.enter





⚠️ Disclaimer
This keylogger is built strictly for educational and ethical purposes. Do not use this tool for malicious or unauthorized activity. Always get consent before monitoring any device.

