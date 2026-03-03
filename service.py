import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class ClientData(BaseModel):
    income: float
    age: int
    car_own_flg: bool
    good_work_flg: bool
    

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/score")
def score(data: ClientData):
    features = [data.income, data.age, data.car_own_flg, data.good_work_flg]
    approved = model.predict([features])[0].item()
    return {"approved": approved}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
 