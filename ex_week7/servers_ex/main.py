from fastapi import FastAPI
from routers import get_routers, post_routers, signup_router, signin_router

app = FastAPI()

app.include_router(get_routers.router)
app.include_router(post_routers.router)
app.include_router(signup_router.router)
app.include_router(signin_router.router)



