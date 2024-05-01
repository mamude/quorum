import uvicorn
from app.routes.bill_v1 import router as bill_router_v1
from app.routes.legislator_v1 import router as legislator_router_v1
from app.routes.legislator_v2 import router as legislator_router_v2
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def index():
    return RedirectResponse("/docs/")


app.include_router(bill_router_v1)
app.include_router(legislator_router_v1)
app.include_router(legislator_router_v2)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
