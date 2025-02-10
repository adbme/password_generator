import secrets
import string

def get_character_pool(include_upper=True, include_lower=True, use_digits=True, use_specials=True):
    pool = []
    if include_upper:
        pool.extend(string.ascii_uppercase)
    if include_lower:
        pool.extend(string.ascii_lowercase)
    if use_digits:
        pool.extend(string.digits)
    if use_specials:
        pool.extend(string.punctuation)
    if not pool:
        raise ValueError("Au moins une catégorie de caractères doit être sélectionnée.")

    return pool

def generate_password(length, use_digits=True, use_specials=True):
    """Génère un mot de passe sécurisé selon les options spécifiées, garantissant l'unicité."""
    
    if not (4 <= length <= 128):
        raise ValueError("La longueur doit être entre 4 et 128 caractères.")

    character_pool = get_character_pool(use_digits=use_digits, use_specials=use_specials)
    
    return ''.join(secrets.choice(character_pool) for _ in range(length))

