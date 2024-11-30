
# Linux Command Assistant

A simple Python-based command-line tool that helps users execute common Linux commands from different categories. The user can choose from various command groups like **File and Directory Management**, **System Information**, **Process Management**, and more. This assistant allows you to easily execute Linux commands without needing to remember their syntax.

## Features

- Categorized commands to execute common Linux tasks.
- Easily select a command from the menu to view its description and execute it.
- Execute commands directly from the terminal with a simple interface.
- Supports commands for managing files, directories, processes, and system information.

## Categories of Commands

1. **File and Directory Management**:
   - Show current directory (`pwd`)
   - List files in a directory (`ls`)
   - Change directory (`cd`)
   - Create a new directory (`mkdir`)
   - Remove a file (`rm`)
   - Remove a directory (`rmdir`)

2. **File Viewing**:
   - View file contents (`cat`, `less`, `more`)

3. **System Information**:
   - Display system info (`uname`, `top`)
   - Show disk usage (`df`)
   - Show memory usage (`free`)

4. **Process Management**:
   - List active processes (`ps`)
   - Show system processes in real-time (`top`)
   - Kill a process by PID (`kill`)

## Requirements

- Python 3.x
- Linux-based operating system (e.g., Ubuntu, Kali Linux)
- Basic knowledge of Linux commands

## How to Run the Project

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
https://github.com/Karthikjl/Linux-terminal-Assistant
cd Linux-terminal-Assistant
```

### 2. Run the Python Script
Run the script in your terminal:

```bash
python3 linux_assistant.py
```

### 3. Select the Command Category
The program will show a menu with various command categories. Select a category by entering the corresponding number.

### 4. Execute the Command
Once you select a command, the assistant will execute it and display the result in the terminal.

## Example

```bash
Linux Command Assistant
==============================
Select a category:
1. File and Directory Management
2. File Viewing
3. System Information
4. Process Management
0. Exit

Enter your choice: 1

File and Directory Management
------------------------------
1. Show current directory
2. List files in a directory
3. Change directory
4. Create a new directory
5. Remove a file
6. Remove a directory
0. Back to Main Menu

Enter the command number: 1

Executing: pwd
/home/user/Desktop/LinuxAssistant
```

## Contributing

Feel free to fork the repository and make improvements. Pull requests are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).
