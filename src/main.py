from fastapi import FastAPI

from src.routers.pages import router_working as pages_router_texts, router_base as pages_router_base
app = FastAPI()


app.include_router(pages_router_base)
app.include_router(pages_router_texts)