from fastapi import FastAPI
from app.controllers import task_controller
from app.database import Base, engine

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_controller.router)
