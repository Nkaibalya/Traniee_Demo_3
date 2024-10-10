from controller.control import home
from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from config import engine
from config_model import Base
from controller.control import router
# from config_model import table

app = FastAPI()
app.include_router(router)
# app.include_router(router,prefix='/v1')
def create_table():
    try:
        Base.metadata.create_all(bind=engine)
        print('Tables created successfully')
    except SQLAlchemyError as e:
        print('Error while creating tables:', e)

# Create tables
create_table()

print('Connected Successfully ...')