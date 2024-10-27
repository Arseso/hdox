from typing import List
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from src.services.vk_profile_reader import analyze_vk_profile

router_base = APIRouter(
    prefix=''
)

router_working = APIRouter(
    prefix='/working'
)



templates = Jinja2Templates(directory='src/templates')

@router_base.get('/')
async def get_base(request: Request):
    return templates.TemplateResponse("index.html", {'request': request, 'active_tab': 'home'})

@router_working.get('/')
async def get_texts(request: Request):
    return templates.TemplateResponse("working.html", {"request": request})

@router_working.post('/')
async def analyze(request: Request, vkLink: str = Form(...)):
    # Here you would add the logic to analyze the VK profile
    result = analyze_vk_profile(vkLink)
    return templates.TemplateResponse("working.html", {"request": request, "result": result})

@router_working.get('/upload/')
async def upload(request: Request):
    raise NotImplementedError

@router_working.get('/id/{id}')
async def get_text_info(id: int, request: Request):
    raise NotImplementedError