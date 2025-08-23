"""Exceptions that can occur during operation."""

class TooManyCommanders(Exception):
    pass


class CommanderNotFoundInDB(Exception):
    pass


class CommanderNotFoundFromSF(Exception):
    pass


class SkipToBeginning(Exception):
    pass


class ExitProgram(Exception):
    pass


class InvalidInput(Exception):
    pass
