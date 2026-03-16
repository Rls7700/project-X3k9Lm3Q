## Installation

You can install this bot as a Python package. It is recommended to use a virtual environment.

1. Clone the repository and navigate to the project directory:

2. Install the package:

```bash
pip install .
```

3. After installation, the bot becomes available as a terminal command. You can start it from anywhere by simply typing:

```bash
assistant-bot
```

4. Alternatively, you can still run it as a script:

```bash
python3 -m modules.console_bot.console_bot
```

# Classes

## Structure

```
FINAL_PROJECT/
├── main.py
├── modules/
│   ├── address_book/
│   │   └── models/
│   │       └── address_book_library.py
|   |       └── common.py
|   |       └── note.py
|   ├── configs
|   |   └── config.py
│   └── console_bot/
│       ├── command_parser.py
│       ├── console_bot.py
│       └── handlers.py
|       └── note_handlers.py
```

### Available commands:

add: [name] [phone] - Add a new contact \
change: [name] [old_phone] [new_phone] - Change an existing contact \
delete: [name] - Delete a contact

phone: [name] - Show a specific contact \
search: [query] - Search contacts by name, phone, email, or address

all: Show all contacts

add-birthday: [name] [birthday] - Add for a specific contact \
show-birthday: [name] - Show birthday for contact \
birthdays: [days] - Show upcoming birthdays for a specified number of days (default 7)

add-email: [name] [email] - Add email for a specific contact \
show-email: [name] - Show email for contact

add-address: [name] [address] - Add physical address for a specific contact \
show-address: [name] - Show address for contact

note_add: [text] - Add a new note \
note_change: [id] [text] - Change an existing note \
note_delete: [id] - Delete a note by id \
note_add_tag: [id] [tag] - Add a tag to a specific note \
note_all: Show all notes \
note_search: [query] - Search notes by text content \
note_sort_tags: Show all notes sorted by tags

dump: Store address book in file \
load: Load address book from file

help: Show available commands \
close: Close the application

hello: Greet the user

## Required

- Python 3.9+

## Authors

Vic Lymar \
Anton Kashuba \
Oleksii Rodionov \
Bohdan Yankevych

@MIT
