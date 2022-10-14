from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def home():
    return{"data": "Welcome to homepage"}


@app.get("/welcome")
def root():
    return {"message": "This is the welcome page"}


@app.get("/posts")
def get_posts():
    return {"data": "This is a random post"}

# Post request (Bad way to create Posts) 
# @app.post("/createpost")
# def create_post(payload: dict = Body(...)):
#    print(payload)
#    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

# Validating data with Schema 

@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post.title)
    print(new_post.content)
    return{"data": "New post"}
