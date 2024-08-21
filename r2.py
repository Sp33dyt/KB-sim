# Import the necessary libraries
import tkinter as tk  # Library for creating GUI
from tkinter import scrolledtext  # Import scrolled text widget
import keyboard  # Library for simulating keyboard events
import threading  # Library for creating threads
import time  # Library for handling time-related tasks
import pynput  # Library for handling mouse events

# Define a class for the Text Simulator Application
class TextSimulatorApp:
    def __init__(self, root):
        # Initialize the root window
        self.root = root
        # Set the title of the root window
        self.root.title("Text Simulator")
        
        # Create a scrolled text area with a width of 50 characters and a height of 10 lines
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        # Pack the text area with a padding of 20 pixels from the top and bottom
        self.text_area.pack(pady=20)
        
        # Create a label for the delay input box
        self.delay_label = tk.Label(root, text="Typing Delay (seconds):")
        # Pack the label above the delay entry
        self.delay_label.pack()

        # Create an entry widget for the user to input the delay time
        self.delay_entry = tk.Entry(root)
        # Set a default delay value
        self.delay_entry.insert(0, "0.25")
        # Pack the entry widget
        self.delay_entry.pack(pady=5)
        
        # Create a start button with the text "START" and a command to start typing
        self.start_button = tk.Button(root, text="START", command=self.start_typing)
        # Pack the start button to the left with a padding of 20 pixels
        self.start_button.pack(side=tk.LEFT, padx=20)
        
        # Create a stop button with the text "STOP" and a command to stop typing
        self.stop_button = tk.Button(root, text="STOP", command=self.stop_typing)
        # Pack the stop button to the right with a padding of 20 pixels
        self.stop_button.pack(side=tk.RIGHT, padx=20)
        
        # Initialize flags for typing and waiting for a mouse click
        self.typing = False
        self.waiting_for_click = False
        
        # Bind the F5 key to the start_typing method
        self.root.bind("<F5>", self.start_typing_shortcut)
        # Bind the F6 key to the stop_typing method
        self.root.bind("<F6>", self.stop_typing_shortcut)

    # Method to start typing
    def start_typing(self):
        # Set the typing flag to True
        self.typing = True
        # Set the waiting for click flag to True
        self.waiting_for_click = True
        # Disable the start button
        self.start_button.config(state=tk.DISABLED)
        # Start a new thread to wait for a mouse click
        threading.Thread(target=self.wait_for_mouse_click).start()

    # Method to stop typing
    def stop_typing(self):
        # Set the typing flag to False
        self.typing = False
        # Enable the start button
        self.start_button.config(state=tk.NORMAL)

    # Method to handle the F5 shortcut key
    def start_typing_shortcut(self, event):
        # Call the start_typing method
        self.start_typing()
        # Return to prevent further event handling
        return "break"

    # Method to handle the F6 shortcut key
    def stop_typing_shortcut(self, event):
        # Call the stop_typing method
        self.stop_typing()
        # Return to prevent further event handling
        return "break"

    # Method to wait for a mouse click
    def wait_for_mouse_click(self):
        try:
            # Define a nested function to handle mouse click events
            def on_click(x, y, button, pressed):
                # If the mouse is pressed and the waiting for click flag is True
                if pressed and self.waiting_for_click:
                    # Set the waiting for click flag to False
                    self.waiting_for_click = False
                    # Stop the mouse listener
                    listener.stop()
                    # Start a new thread to simulate typing
                    threading.Thread(target=self.simulate_typing).start()

            # Create a mouse listener with the on_click function
            listener = pynput.mouse.Listener(on_click=on_click)
            # Start the mouse listener
            listener.start()
            # Join the mouse listener thread
            listener.join()
        except Exception as e:
            # Handle any exceptions that occur during mouse listening
            print(f"Error waiting for mouse click: {e}")

    # Method to simulate typing
    def simulate_typing(self):
        try:
            # Get the text from the text area
            text = self.text_area.get("1.0", tk.END)
            # Retrieve the delay time from the entry widget
            delay = float(self.delay_entry.get())  # Convert input to a float        
            # Iterate over each character in the text
            i = 0
            while i < len(text):
                if not self.typing:
                    break

                # Check for the special character sequence '\t' to simulate a TAB key press
                if text[i:i+2] == '\\t':  # Look for '\t' sequence
                    keyboard.press_and_release('tab')
                    i += 2  # Skip the '\t' characters
                else:
                    # Simulate typing the character normally
                    keyboard.write(text[i])
                    i += 1

                time.sleep(delay)

        except Exception as e:
            # Handle any exceptions that occur during typing simulation
            print(f"Error simulating typing: {e}")
        finally:
            self.stop_typing()

# If the script is run as the main program
if __name__ == "__main__":
    try:
        # Create a new Tkinter root window
        root = tk.Tk()
        # Create a new instance of the TextSimulatorApp class
        app = TextSimulatorApp(root)
        # Start the Tkinter event loop
        root.mainloop()
    except Exception as e:
        # Handle any exceptions that occur during application execution
        print(f"Error running application: {e}")