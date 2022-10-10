from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def home():
    return{"data": "Welcome to homepage"}


@app.get("/welcome")
def root():
    return {"message": "This is the welcome page"}


@app.get("/posts")
def get_posts():
    return {"data": "This is a random post"}

# Post request 
@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}