import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def index():
    return RedirectResponse("/docs/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
