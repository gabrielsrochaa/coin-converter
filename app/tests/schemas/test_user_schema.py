from datetime import datetime
import pytest
from app.schemas.user import User, TokenData

def test_user_schema():
    user = User(
        username='Gabriel',
        password='batatapotatoassadafrita'
    )
    assert user.dict() == {
        'username': 'Gabriel',
        'password': 'batatapotatoassadafrita'
    }

def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(
            username='João#',
            password='batatapotatoassadafrita'
        )

def test_token_data():
    expires_at = datetime.now()
    token_data = TokenData(
        access_token='token_qualquer',
        expires_at=expires_at
    )

    assert token_data.dict() == {
        'access_token': 'token_qualquer',
        'expires_at': expires_at
    }
