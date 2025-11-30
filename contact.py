import os
import json
import datetime
import sys 
from pathlib import Path
from rich.console import Console
CONSOLE = Console()

CONTACTS_FILE = "contacts.json"  # Define the contacts file path

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return{}
    try:
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        CONSOLE.print("[red]Error: Invalid JSON format in contacts file.[/red]")
        return {}
    except Exception as e:
        CONSOLE.print(f"[red]Error: Failed to load contacts: {e}[/red]")
        return {}
def save_contacts(contacts):
    try:
        with open(CONTACTS_FILE, 'w') as f:
            json.dump(contacts, f, indent=4)
        CONSOLE.print("[green]Contacts saved successfully.[/green]")
    except Exception as e:
        CONSOLE.print(f"[red]Error: Failed to save contacts: {e}[/red]")
def add_contact(contacts, name, phone, email):
    if not name or not phone or not email:
        CONSOLE.print("[red]Error: Name, phone, and email are required.[/red]")
        return contacts
    if name in contacts:
        CONSOLE.print(f"[red]Error: Contact with name '{name}' already exists.[/red]")
        return contacts
    contacts[name] = {
        "phone": phone, 
        "email": email, 
        "added_on": str(datetime.datetime.now())
        }
    CONSOLE.print(f"[green]Contact '{name}' added successfully. [/green]")
    return contacts
def list_contacts(contacts):
    if not contacts:
        CONSOLE.print("[yellow] No contacts found.[/yellow]")
        return
    for name, info in contacts.items():
        CONSOLE.print(f"[blue]Name:[\blue] {name}, [blue]Phone:[\blue] {info['phone']}, [blue]Email:[\blue] {info['email']}, [blue]Added On:[\blue] {info['added_on']}")
def main():
    contacts = load_contacts()
    while True:
        CONSOLE.print("\n[bold]Contact Manager[/bold]")
        CONSOLE.print("1. Add Contact")
        CONSOLE.print("2. List Contacts")
        CONSOLE.print("3. Save Contacts")
        CONSOLE.print("4. Exit")
        choice = CONSOLE.input("Choose an option: ")
        if choice == '1':
            name = CONSOLE.input("Enter name: ")
            phone = CONSOLE.input("Enter phone: ")
            email = CONSOLE.input("Enter email: ")
            contacts = add_contact(contacts, name, phone, email)
        elif choice == '2':
            list_contacts(contacts)
        elif choice == '3':
            save_contacts(contacts)
        elif choice == '4':
            CONSOLE.print("[green]Exiting Contact Manager. Goodbye![/green]")
            break
        else:
            CONSOLE.print("[red]Invalid choice. Please try again.[/red]")
if __name__ == "__main__":
    main()



