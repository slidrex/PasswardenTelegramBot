from string import ascii_letters, punctuation, digits
import secrets
import string_utils

def generate_pass(length: int, include_symbols: bool):
    alphabet = ascii_letters + digits
    if include_symbols:
        alphabet += punctuation
    alphabet = string_utils.shuffle(alphabet)
    return ''.join(secrets.choice(alphabet) for i in range(length + 1))