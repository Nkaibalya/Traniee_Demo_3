from config_model import db
from sqlalchemy.orm import Session
from config_model import PersonDetails
def get(a:Session):
    res = a.query(PersonDetails).all()
    if not res:
        return {'msg': 'No data found'}
    # return {'data': [i.dict() for i in res]}
    return res

def posts(session : Session, data : db):
    try:
        res = PersonDetails(**data.dict())
        session.add(res)
        session.commit()
        session.refresh(res)
        return {'data': res}
    except Exception as e:
        session.rollback()
        return {'error': str(e)}
def update(session : Session , db : db , name : str):
    try:
        res = session.query(PersonDetails).filter(PersonDetails.name == name).first()
        if not res:
            return {'msg': 'Name Not Found ...'}
        res.name = db.name
        res.age = db.age
        res.hobby = db.hobby
        res.dob = db.dob
        session.commit()
        session.refresh(res)
        return {'data': res}
    except Exception as e:
        session.rollback()
        return {'error': str(e)}
    

def delete(session : Session , db : db , id : int):
    try:
        res = session.query(PersonDetails).filter(PersonDetails.id == id).first()
        if not res:
            return {'msg': 'Id Not Found ...'}
        session.delete(res)
        session.commit()
        return {'msg': 'Data deleted successfully'}
    except Exception as e:
        session.rollback()
        return {'error': str(e)}