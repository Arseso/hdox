from bs4 import BeautifulSoup
from requests import get, exceptions
from pydantic import BaseModel

class AnalysisResult(BaseModel):
    name: str

def vk_profile_analize(link: str) -> AnalysisResult:
    try:
        page = get(link)
    except exceptions.InvalidURL:
        return AnalysisResult(name= "Undefined")
    soup = BeautifulSoup(page.content)
    h2 = soup.find_all('p', class="", recursive=True)
        