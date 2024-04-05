from fastapi import FastAPI
from routers import get_routers, post_routers

app = FastAPI()
print('jjj')
app.include_router(get_routers.router)
app.include_router(post_routers.router)


