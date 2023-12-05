import pytest
from app.schemas.user import User

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
