from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional

from crud import (
    create_user, verify_user,
    create_post, read_posts,
    update_post, delete_post,
    like_post
)

app = FastAPI()


# ---------- MODELS ----------

class UserCreate(BaseModel):
    username: str
    password: str


class PostCreate(BaseModel):
    content: str


class PostUpdate(BaseModel):
    content: str


# ---------- AUTH ----------

@app.post("/register")
def register(user: UserCreate):
    if not create_user(user.username, user.password):
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"status": "ok"}


@app.post("/login")
def login(user: UserCreate):
    user_id = verify_user(user.username, user.password)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"user_id": user_id}


# ---------- POSTS ----------

@app.post("/posts")
def create_new_post(
    post: PostCreate,
    x_user_id: int = Header(...)
):
    if not create_post(x_user_id, post.content):
        raise HTTPException(status_code=400, detail="Failed to create post")
    return {"status": "ok"}


@app.get("/posts")
def get_posts():
    posts = read_posts()
    return [
        {
            "post_id": p[0],
            "user_id": p[1],
            "content": p[2],
            "likes": p[3]
        }
        for p in posts
    ]


@app.put("/posts/{post_id}")
def edit_post(
    post_id: int,
    post: PostUpdate,
    x_user_id: int = Header(...)
):
    if not update_post(post_id, post.content, x_user_id):
        raise HTTPException(status_code=403, detail="Not allowed or post not found")
    return {"status": "ok"}


@app.delete("/posts/{post_id}")
def remove_post(
    post_id: int,
    x_user_id: int = Header(...)
):
    if not delete_post(post_id, x_user_id):
        raise HTTPException(status_code=403, detail="Not allowed or post not found")
    return {"status": "ok"}


# ---------- LIKES ----------

@app.post("/posts/{post_id}/like")
def like_post_endpoint(
    post_id: int,
    x_user_id: int = Header(...)
):
    if not like_post(post_id, x_user_id):
        raise HTTPException(status_code=400, detail="Already liked or invalid post")
    return {"status": "ok"}


@app.get("/")
def root():
    return {"status": "API is running"}


#run uvicorn api:app --reload --host 0.0.0.0 --port 8000            -to let other computers in the network access the API
#they then can access api through http://[my computer's IP]:8000   (replace [my computer's IP] with the actual IP address)
#you still need some complex code tho...
#to access documentation, run http://127.0.0.1:8000/docs