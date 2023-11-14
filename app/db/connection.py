from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URL = config('DB_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)
# Session = sessionmaker(bind=engine)
Session = scoped_session(sessionmaker(bind=engine))
Session()
