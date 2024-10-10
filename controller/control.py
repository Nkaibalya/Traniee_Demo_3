from fastapi import APIRouter,Depends
import service.sevicer as service
from config_model import db
from sqlalchemy.orm import Session
from config import get_db


router = APIRouter()
@router.get('/get')
def get_data( a : Session = Depends(get_db)):
    res =  service.get(a)
    # lst  = []
    # for i in res:
    #     lst.append(i)
    # return {'data': lst}
    return res
    


@router.post('/post')
def post_data(db : db, session : Session = Depends(get_db)):
    return service.posts(session,db)


@router.put('/patch/{name}')
def patch_data(name: str,data:db,session:Session = Depends(get_db)):
    return service.update(session, data, name)


@router.delete('/delete/{id}')
def delete_data(data : db, id:int, session : Session = Depends(get_db)):
    return service.delete(session,db,id)

def home():
    return {"message": "Wellcome To Here !"}