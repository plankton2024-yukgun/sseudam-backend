from fastapi import FastAPI
from .post.routers import router as post_router
from .interaction.routers import router as interaction_router
from .user.routers import router as user_router
from .db import init_dev_db

init_dev_db()

app = FastAPI(title="Sseudam API")

app.include_router(post_router, prefix="/posts")
app.include_router(interaction_router, prefix="/posts")
app.include_router(user_router, prefix="/users")


@app.get("/")
async def root():
    return {"message": "Welcome to Sseudam API"}
