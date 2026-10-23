"""Small helpers for validating function arguments in our review checklist drill."""


def valid_port(value):
    """Return True only for integers from 1 to 65535, False for anything else.

    Strings, floats, None, and booleans are all rejected. Booleans need an
    explicit guard because in Python ``bool`` is a subclass of ``int``.
    """
    if isinstance(value, bool):
        return False
    if not isinstance(value, int):
        return False
    return 1 <= value <= 65535
