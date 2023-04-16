from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field,validator
import importlib

app = FastAPI()


class ExerciseRequest(BaseModel):
    token: str
    id_exercise: str
    answer: str

class ExerciseResponse(BaseModel):
    token: str
    id_exercise: str
    answer: str
    status: str # status if the info was posted on not on the DB

@app.post("/exercise-post/")
async def exercise_post(answer:ExerciseRequest ) -> ExerciseResponse:
    

    return 