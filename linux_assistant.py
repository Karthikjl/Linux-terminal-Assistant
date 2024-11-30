import os

# Dictionary to store categories and commands
commands = {
    "File and Directory Management": {
        "1. Show current directory": "pwd",
        "2. List files in a directory": "ls",
        "3. Change directory": "cd",
        "4. Create a new directory": "mkdir new_directory_name",
        "5. Remove a file": "rm file_name",
        "6. Remove a directory": "rmdir directory_name"
    },
    "File Viewing": {
        "1. View file content": "cat file_name",
        "2. View first 10 lines of a file": "head file_name",
        "3. View last 10 lines of a file": "tail file_name",
        "4. Edit file using nano": "nano file_name"
    },
    "System Information": {
        "1. Display system info": "uname -a",
        "2. Show disk usage": "df -h",
        "3. Show memory usage": "free -m"
    },
    "Process Management": {
        "1. List active processes": "ps",
        "2. Show system processes (real-time)": "top",
        "3. Kill a process by PID": "kill PID"
    }
}

def display_menu():
    print("\nLinux Command Assistant")
    print("=" * 30)
    print("Select a category:")
    for i, category in enumerate(commands.keys(), start=1):
        print(f"{i}. {category}")
    print("0. Exit")

def execute_command(category, choice):
    try:
        # Retrieve the selected command
        command_list = list(commands[category].values())
        command = command_list[choice - 1]
        # Execute the command
        print(f"\nExecuting: {command}")
        os.system(command)
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        display_menu()
        try:
            category_choice = int(input("\nEnter your choice: "))
            if category_choice == 0:
                print("Exiting the program. Goodbye!")
                break

            selected_category = list(commands.keys())[category_choice - 1]
            print(f"\n{selected_category}")
            print("-" * 30)
            
            # Display commands without adding extra numbers
            for command in commands[selected_category].keys():
                print(command)
            print("0. Back to Main Menu")

            command_choice = int(input("\nEnter the command number: "))
            if command_choice == 0:
                continue

            execute_command(selected_category, command_choice)
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
