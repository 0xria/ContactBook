# Contact Manager
A simple contact manager application that allows you to add, search, and delete contacts. Contacts are stored in a dictionary and persisted to a file for future use.

## Features
- Add new contacts with name, phone number, and email.
- Search for contacts by name.
- Delete contacts by name or single command.
- Contacts are stored in a dictionary for quick access.
- Contacts are saved to a file for persistence across sessions.
- Simple command-line interface for easy interaction.
- Persistent storageusing JSON format.
- Clean, intuitive command-line interface.

## Cybersecurity Twist
- Practice secure file handling; think about what happens if files are corrupted or accessed by unauthorized users.
- Use a virtual environment from the start to keep dependencies isolated.
- Gracefully handles corrupted storage files.
- Encourages best practices for secure file handling and data protection.
- Shows how even simple applications benefit from secure coding practices.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/0xria/ContactBook.git
2. cd into the project directory:
   ```bash
   cd ContactBook
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   run: python3 contact.py
   ```

4. Track your dependencies in a requirements.txt as you go:

    pip freeze > requirements.txt
