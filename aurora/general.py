
def print_if_not_quiet(quiet:bool, message:str)->None:
    """Print the message if quiet is False."""
    if not quiet:
        print(message)