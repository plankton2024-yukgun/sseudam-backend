from fastapi import FastAPI
from .post.routers import router as post_router
from .interaction.routers import router as interaction_router
from .user.routers import router as user_router
from .board.routers import router as board_router

app = FastAPI(title="Sseudam API")

app.include_router(post_router)
app.include_router(interaction_router)
app.include_router(user_router)
app.include_router(board_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Sseudam API"}
