from app.core.security import hash_password, verify_password

def test_password_hash():

    password = "123456"

    hashed = hash_password(password)

    assert verify_password(password, hashed) == True