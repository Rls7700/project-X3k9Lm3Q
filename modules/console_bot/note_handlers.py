# Handler functions for working with notes
import pickle
import os
from colorama import Fore # type: ignore
from functools import wraps
from ..address_book.models.note import Note
from ..configs.config import NOTE_BOOK_FILE


# Dictionary of notes
notes = {}


# Decorator to handle input errors
def note_input_error(func):
    @wraps(func)
    def inner(*args):
        try:
            if func.__name__ in ["note_add", "note_delete", "note_search"] and len(args[0]) < 1:
                raise ValueError()

            if func.__name__ in ["note_change", "note_add_tag"] and len(args[0]) < 2:
                raise ValueError()

            if len(args[0]) < 1:
                raise Exception('Format error')

            return func(*args)

        except ValueError:
            print(f"{Fore.RED}Please enter input params properly.{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Fore.RESET} ")
    return inner


def note_all():
    for note in notes.values():
        print(note)


@note_input_error
def note_add(args):
    value = " ".join(args[:len(args)]).capitalize()
    note = Note(value)    
    notes[note.id] = note
    print(f"Note {Fore.GREEN}{note.id}{Fore.RESET} was added")


@note_input_error
def note_change(args):
    id = args[0]
    value = " ".join(args[1:]).capitalize()
    if not notes[id]:
        print(f"Note was not found: {Fore.RED}{id}{Fore.RESET}")
        return
    notes[id].change(value);
    print(f"Changed note {Fore.GREEN}{id}{Fore.RESET}")


@note_input_error
def note_delete(args):
    id = args[len(args)-1]
    if id in notes:
        del notes[id]
        print(f"Deleted note: {Fore.GREEN}{id}{Fore.RESET}")
    else:
        print(f"Note was not found: {Fore.RED}{id}{Fore.RESET}")
        return    


def dump():
    try:
        with open(NOTE_BOOK_FILE, "wb") as file:
            pickle.dump(notes, file)
        print(f"{Fore.GREEN}Notes were saved to {NOTE_BOOK_FILE}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error saving notes: {e}{Fore.RESET}")


def load():
    global notes
    try:
        if not os.path.exists(NOTE_BOOK_FILE):
            print(f"{Fore.YELLOW}Notes were not found at {NOTE_BOOK_FILE}{Fore.RESET}")
            return
        with open(NOTE_BOOK_FILE, "rb") as file:
            notes = pickle.load(file)
        print(f"{Fore.GREEN}Notes loaded from {NOTE_BOOK_FILE}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error loading notes: {e}{Fore.RESET}")


@note_input_error
def note_add_tag(args):
    note_id = args[0]
    tag = args[1]
    
    if note_id not in notes:
        print(f"Note was not found: {Fore.RED}{note_id}{Fore.RESET}")
        return
        
    notes[note_id].add_tag(tag)
    print(f"Added tag {Fore.GREEN}{tag}{Fore.RESET} to note {Fore.GREEN}{note_id}{Fore.RESET}")


@note_input_error
def note_search(args):
    query = args[0].lower()
    found = False
    for note in notes.values():
        if query in note.value.lower() or any(query in tag.lower() for tag in note.tags):
            print(note)
            found = True
    if not found:
        print(f"No notes found for query: {Fore.YELLOW}{query}{Fore.RESET}")


def note_sort_tags():
    sorted_notes = sorted(
        notes.values(), 
        key=lambda n: (len(n.tags) == 0, n.tags[0].lower() if n.tags else "")
    )
    
    if not sorted_notes:
        print("No notes to show.")
        return
        
    for note in sorted_notes:
        print(note)
