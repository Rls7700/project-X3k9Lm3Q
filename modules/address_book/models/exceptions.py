class AddressBookException(Exception):
    """Base exception for address book domain."""
    pass


class RecordException(AddressBookException):
    """Raised when record/contact is not found or invalid."""
    pass


class PhoneException(AddressBookException):
    """Raised when phone is invalid."""
    pass


class EmailException(AddressBookException):
    """Raised when email is invalid."""
    pass


class AddressException(AddressBookException):
    """Raised when address is invalid."""
    pass


class BirthdayException(AddressBookException):
    """Raised when birthday is invalid."""
    pass


class NoteException(AddressBookException):
    """Raised when note is invalid."""
    pass