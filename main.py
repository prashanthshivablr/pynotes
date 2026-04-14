from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "FastAPI is running successfully"}

@app.get("/users")
def get_users():
    return [
        {"name": "Prashanth", "age": 26},
        {"name": "Vinay", "age": 29}
    ]

@app.post("/user")
def create_user(user: User):
    return {
        "status": "success",
        "user": user
    }

@app.get("/ai")
def ai_message():
    return {"response": "This is how AI APIs respond!"}