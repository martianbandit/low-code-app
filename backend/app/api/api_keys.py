from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import session, models
from app.schemas.api_key import ApiKeyCreate

router = APIRouter()

@router.get("/")
def get_api_keys(db: Session = Depends(session.get_db)):
    return db.query(models.ApiKey).all()

@router.post("/")
def create_api_key(api_key: ApiKeyCreate, db: Session = Depends(session.get_db)):
    db_api_key = models.ApiKey(name=api_key.name, key=api_key.key)
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key
