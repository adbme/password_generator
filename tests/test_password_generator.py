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
        generate_password(3)  # Trop court
    with pytest.raises(ValueError):
        generate_password(129)  # Trop long

def get_character_pool():
    """Retourne l'ensemble des caractères utilisables pour le mot de passe."""
    return string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    """Génère un mot de passe sécurisé de la longueur spécifiée."""
    if not (4 <= length <= 128):
        raise ValueError("La longueur doit être entre 4 et 128 caractères.")
    
    return ''.join(secrets.choice(get_character_pool()) for _ in range(length))