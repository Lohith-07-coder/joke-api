from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Some random jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None. It’s a hardware problem.",
    "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
    "There are only 10 kinds of people in the world: those who understand binary and those who don’t.",
    "Why did the developer go broke? Because he used up all his cache."
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    joke = random.choice(jokes)
    return templates.TemplateResponse("index.html", {"request": request, "joke": joke})
