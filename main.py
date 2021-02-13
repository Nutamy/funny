# 'https://dog.ceo/api/breeds/image/random' 

from typing import Optional
from fastapi import FastAPI, Request
import requests
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory = 'templates')

class RequestAPI:
    url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2'

    def get_all(self):
        result = requests.get(self.url).json()
        return result.text
        
@app.get('/')
def index(request: Request):
    my_req = RequestAPI()
    dog_img = my_req.get_all()
    templates.TemplateResponse('index.html', {
        'request': request, 
        'dog_img': dog_img
    })