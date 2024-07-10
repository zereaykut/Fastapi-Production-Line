from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Products
from database import SessionLocal
from .auth import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class ProductRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Products).filter(Products.owner_id == user.get('id')).all()


@router.get("/product/{product_id}", status_code=status.HTTP_200_OK)
async def read_product(user: user_dependency, db: db_dependency, product_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    product_model = db.query(Products).filter(Products.id == product_id)\
        .filter(Products.owner_id == user.get('id')).first()
    if product_model is not None:
        return product_model
    raise HTTPException(status_code=404, detail='Product not found.')


@router.post("/product", status_code=status.HTTP_201_CREATED)
async def create_product(user: user_dependency, db: db_dependency,
                      product_request: ProductRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    product_model = Products(**product_request.dict(), owner_id=user.get('id'))

    db.add(product_model)
    db.commit()


@router.put("/product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_product(user: user_dependency, db: db_dependency,
                      product_request: ProductRequest,
                      product_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    product_model = db.query(Products).filter(Products.id == product_id)\
        .filter(Products.owner_id == user.get('id')).first()
    if product_model is None:
        raise HTTPException(status_code=404, detail='Product not found.')

    product_model.title = product_request.title
    product_model.description = product_request.description
    product_model.priority = product_request.priority
    product_model.complete = product_request.complete

    db.add(product_model)
    db.commit()


@router.delete("/product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(user: user_dependency, db: db_dependency, product_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    product_model = db.query(Products).filter(Products.id == product_id)\
        .filter(Products.owner_id == user.get('id')).first()
    if product_model is None:
        raise HTTPException(status_code=404, detail='Product not found.')
    db.query(Products).filter(Products.id == product_id).filter(Products.owner_id == user.get('id')).delete()

    db.commit()












