import pytest
from src.password_generator import generate_password
import secrets
import string

def test_short_password():
    password = generate_password(8)
    assert len(password) == 8

def test_long_password():
    password = generate_password(32)
    assert len(password) == 32

def test_invalid_length():
    with pytest.raises(ValueError):
        generate_password(3) # Trop court
    with pytest.raises(ValueError):
        generate_password(129) # Trop long


def test_letters_only():
    password = generate_password(12, use_digits=False, use_specials=False)
    assert len(password) == 12
    assert all(c in string.ascii_letters for c in password)

def test_all_categories():
    password = generate_password(16, use_digits=True, use_specials=True)
    assert len(password) == 16
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)

def test_no_special_chars():
    password = generate_password(20, use_digits=True, use_specials=False)
    assert len(password) == 20
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert not any(c in string.punctuation for c in password)
    
def get_character_pool(include_upper=True, include_lower=True, use_digits=True, use_specials=True):
    """Retourne l'ensemble des caractères utilisables pour le mot de passe."""
    pool = ""
    if include_upper:
        pool += string.ascii_uppercase
    if include_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_specials:
        pool += string.punctuation

    if not pool:
        raise ValueError("Au moins une catégorie de caractères doit être sélectionnée.")

    return pool

def generate_password(length, use_digits=True, use_specials=True):
    """Génère un mot de passe sécurisé selon les options spécifiées."""
    if not (4 <= length <= 128):
        raise ValueError("La longueur doit être entre 4 et 128 caractères.")

    character_pool = get_character_pool(use_digits=use_digits, use_specials=use_specials)
    return ''.join(secrets.choice(character_pool) for _ in range(length))