from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config_model import PersonDetails
# import psycopg2

DATABASE_URL = "postgresql://postgres:Password@172.16.0.103:5432/test"
try:
    engine = create_engine(DATABASE_URL)
    PersonDetails
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print('Connected Successfully ...(from config.py)')
except Exception as e:
    print("Error while connecting to PostgreSQL", e)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# try:
#     conString = psycopg2.connect(
#         dbname='test',
#         user='postgres',
#         password='Password',
#         host='172.16.0.103',
#         port='5432'
#     )
#     print('Connected Successfully ...')
# except Exception as e:
#     print("Error while connecting to PostgreSQL", e)
