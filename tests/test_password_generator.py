import pytest
from password_generator import generate_password
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

def generate_password(length):
    if length < 4 or length > 128:
        raise ValueError("La longueur doit être entre 4 et 128 caractères.")
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))