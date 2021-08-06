import time
import uvicorn

from fastapi import FastAPI, Depends, Request, Form
from typing import Optional, List

import auth
import upload
import tasks
from utils import oauth2_scheme

app = FastAPI()

app.include_router(auth.router, prefix='/api/v1')
app.include_router(upload.router, prefix='/api/v1')
app.include_router(tasks.router, prefix='/api/v1')


@app.get('/')
async def root(s: Optional[str] = Depends(oauth2_scheme)):
    return {'s': s}


@app.post('/login')
async def login(username: str = Form(...), password: str = Form(...)):
    return {'username': username, 'password': password}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = f'{time.time() - start_time:.4f}'
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True, debug=True)
