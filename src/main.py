from fastapi import FastAPI
from src.routers import router as operation_router
from src.routers.pages import router_texts as pages_router_texts, router_base as pages_router_base
app = FastAPI()


app.include_router(operation_router)
app.include_router(pages_router_base)
app.include_router(pages_router_texts)