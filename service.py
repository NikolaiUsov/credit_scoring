import joblib
from fastapi import FastAPI
from pydantic import BaseModel


class ClientData(BaseModel):
    income: float
    age: int
    car_own_flg: bool
    good_work_flg: bool


app = FastAPI()
model = joblib.load("model.pkl")


@app.post("/score")
def score(data: ClientData):
    features = [data.income, data.age, data.good_work_flg, data.car_own_flg]
    approved = not model.predict([features])[0].item()
    return {"approved": approved}
 