import pytest
from app.db.connection import Session

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield Session
    finally:
        session.close()