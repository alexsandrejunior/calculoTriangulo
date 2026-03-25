from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Exercicio 01 - Cliente/Servidor (Triangulo)", version="1.0.0")


class TriangleAreaRequest(BaseModel):
    base: float
    height: float


class TriangleAreaResponse(BaseModel):
    base: float
    height: float
    area: float


@app.post("/api/v1/triangle/area", response_model=TriangleAreaResponse)
def triangle_area(req: TriangleAreaRequest) -> TriangleAreaResponse:
    if req.base <= 0:
        raise HTTPException(status_code=400, detail="base deve ser maior que zero")
    if req.height <= 0:
        raise HTTPException(status_code=400, detail="height deve ser maior que zero")

    area = (req.base * req.height) / 2.0
    return TriangleAreaResponse(base=req.base, height=req.height, area=area)

