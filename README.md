# Classes

## Structure

```
homework4/
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

### Task

```bash
python3 -m modules.console_bot.console_bot
```

### Available commands:

add: [name] [phone] - Add a new contact
change: [name] [old_phone] [new_phone] - Change an existing contact
delete: [name] - Delete a contact
phone: [name] - Show a specific contact
search: [query] - Search contacts by name, phone, email, or address
all: Show all contacts
add-birthday: [name] [birthday] - Add for a specific contact
show-birthday: [name] - Show birthday for contact
add-email: [name] [email] - Add email for a specific contact
show-email: [name] - Show email for contact
add-address: [name] [address] - Add physical address for a specific contact
show-address: [name] - Show address for contact
birthdays: [days] - Show upcoming birthdays for a specified number of days (default 7)
note_add: [text] - Add a new note
note_change: [id] [text] - Change an existing note
note_delete: [id] - Delete a note by id
note_add_tag: [id] [tag] - Add a tag to a specific note
note_all: Show all notes
note_search: [query] - Search notes by text content
note_sort_tags: Show all notes sorted by tags
dump: Store address book in file
load: Load address book from file
help: Show available commands
close: Close the application
hello: Greet the user

## Required

- Python 3.9+

## Author

Vic Lymar
victorlymar@gmail.com
@MIT
