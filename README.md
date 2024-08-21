# Text Simulator Application

## Overview

The **Text Simulator** is a Python-based GUI application that allows users to simulate keyboard typing with a configurable delay. This tool can be particularly useful for demonstrations, testing, or automating repetitive typing tasks.

The application uses the `Tkinter` library to create the graphical user interface (GUI) and `keyboard` along with `pynput` to handle keyboard events and mouse interactions.

## Features

- **Scrollable Text Area**: Input the text you want to simulate typing.
- **Configurable Typing Delay**: Adjust the delay between each keystroke.
- **Mouse Click Trigger**: Start typing automatically after a mouse click.
- **Shortcut Keys**: 
  - Press `F5` to start typing.
  - Press `F6` to stop typing.
- **Handles Special Characters**: Supports the `	` sequence to simulate pressing the TAB key.

## Installation

To run this application, you need to have Python installed along with the required libraries. Follow these steps to set up the environment:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Sp33dyt/KB-sim
    cd KB-sim
    ```

2. **Install Required Libraries**:
    Use `pip` to install the necessary dependencies:
    ```bash
    pip install tkinter pynput keyboard
    ```

3. **Run the Application**:
    ```bash
    python r2.py
    ```

## How to Use

1. **Launch the Application**:
   - After running the script, a window will appear with a text area and controls.

2. **Input the Text**:
   - Type or paste the text you want to simulate into the text area.

3. **Set the Typing Delay**:
   - Enter the desired delay (in seconds) between keystrokes in the "Typing Delay" input box. The default is `0.25` seconds.

4. **Start Typing**:
   - Click the `START` button or press `F5` to begin the typing simulation.
   - The simulation will start after detecting a mouse click.

5. **Stop Typing**:
   - Click the `STOP` button or press `F6` to stop the typing simulation at any time.

## Code Overview

- **`TextSimulatorApp` Class**:
  - Manages the entire GUI and functionality of the application.
  - Handles starting and stopping the typing simulation.
  - Manages user input for delay and text to be typed.

- **Main Loop**:
  - Initializes the `Tkinter` GUI and starts the application's event loop.

## Troubleshooting

- **Error Handling**:
  - The application includes basic error handling. If any issues arise (e.g., missing libraries or errors during typing simulation), the error message will be printed to the console.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue. All contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or issues, please contact [sp33dyt@gmail.com](mailto:sp33dyt@gmail.com).
