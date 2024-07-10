from fastapi import FastAPI
import models
from database import engine
from routers import auth, products, admin, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(admin.router)
app.include_router(users.router)
