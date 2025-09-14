from fastapi import FastAPI
import models
from database import engine
from auth import router as auth_router

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Knowledge Vault")

# Include routes
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Welcome to Knowledge Vault API"}
