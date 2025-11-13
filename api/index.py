from fastapi import FastAPI
import random

app = FastAPI()

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
    "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Python Joke API!"}

@app.get("/joke")
def get_joke():
    return {"joke": random.choice(jokes)}
