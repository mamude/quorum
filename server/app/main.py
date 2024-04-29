import uvicorn
from app.routes.legislator import router as legislator_router
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def index():
    return RedirectResponse("/docs/")


app.include_router(legislator_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
