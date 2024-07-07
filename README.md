# Website Ping Tool

## Description
The Website Ping Tool is a Python application that allows users to monitor website availability. It pings a specified website URL at regular intervals and notifies the user when the site becomes reachable. This tool is particularly useful for checking when a temporarily down website comes back online.

## Features
- User-friendly GUI built with customtkinter
- Continuous pinging of specified websites
- Visual and audio notifications when a site becomes reachable
- Automatic web browser opening upon successful ping
- Ability to reset and start new ping processes

## Dependencies
This project relies on the following Python libraries:
- customtkinter
- requests
- pygame
- Pillow (PIL)
- webbrowser (standard library)
- threading (standard library)
- time (standard library)

You can install the required libraries using pip:
## How to Use
1. Enter the URL of the website you want to monitor in the input field.
2. Click the "Ping" button to start monitoring.
3. The application will continuously ping the website and display the status in the text area.
4. When the website becomes reachable, you'll receive a notification, hear a sound, and the website will open in your default browser.
5. Use the "Reset" button to stop the current ping process and prepare for a new one.

## Building the Executable
To create a standalone executable, we use PyInstaller. Follow these steps:

1. Ensure you have PyInstaller installed:
2. Run the following command to create the executable:  python -m PyInstaller --name=PingApp --onefile --windowed --icon=ping.ico --add-data "ping.png;." --add-data "notification.mp3;." --add-data "ping.ico;." ping.py
This command creates a single executable file named PingApp.exe in the `dist` folder.
3. Alternatively, you can use the spec file for more control: python -m PyInstaller PingApp.spec

Make sure to modify the PingApp.spec file to include all necessary resources.

## Additional Notes
- Ensure that `ping.png`, `notification.mp3`, and `ping.ico` are in the same directory as your script when building the executable.
- The executable can be run on systems without Python installed.
- For development purposes, you can run the script directly with Python:  python ping.py

 ## Troubleshooting
If you encounter any issues with the executable:
1. Try running it from the command line to see any error messages:
2. Ensure all required files are present in the same directory as the executable.
3. Check that all dependencies are correctly installed if running the Python script directly.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-your-issues-page) if you want to contribute.

## License
 MIT

## Author
Oussama Amir Sekkal

## Acknowledgments
- customtkinter for the modern GUI elements
- PyInstaller for enabling easy distribution as an executable
