Title: FastAPI Basics: My First GET & POST API
Date: 2026-04-15
Category: GenAI

Today I built my first backend API using FastAPI.

## What I learned
- Creating GET endpoints
- Creating POST endpoints
- Using Pydantic for validation
- Testing APIs using Swagger UI

## Code Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "FastAPI is running successfully"}

@app.post("/user")
def create_user(user: User):
    return {"status": "success", "user": user}