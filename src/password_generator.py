import string
import secrets

def generate_password(length):
    if length < 4 or length > 128:
        raise ValueError("La longueur doit être entre 4 et 128 caractères.")
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))
