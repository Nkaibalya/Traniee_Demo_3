from sqlalchemy import Column,String,Integer,Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PersonDetails(Base):
    __tablename__ = "person_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    hobby = Column(String)
    dob = Column(String)
# def table():
#     try:
#         conn = conString.cursor()
#         conn.execute("""CREATE TABLE IF NOT EXISTS person_details (
#                         id SERIAL PRIMARY KEY,
#                         name VARCHAR(100) NOT NULL,
#                         age INTEGER NOT NULL,
#                         hobby VARCHAR(100) NOT NULL,
#                         dob DATE NOT NULL);""")
#         conString.commit()
#         print('Table created successfully')
#     except Exception as e :
#         print('Error while creating tables', e)

from pydantic import BaseModel
from datetime import date
class db(BaseModel):
    id: int
    name:str
    age:int
    hobby:str
    dob: str