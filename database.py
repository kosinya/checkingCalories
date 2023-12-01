import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

import config

engine = db.create_engine(config.DB_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_connection():
    connection = Session()
    try:
        yield connection
    except Exception as e:
        print(e)
    finally:
        connection.close()
