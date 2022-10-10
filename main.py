from fastapi import FastAPI

app = FastAPI()


@app.get("/welcome")
async def root():
    return {"message": "Welcome to my API"}