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
