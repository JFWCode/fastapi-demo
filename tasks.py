import time
from typing import Optional

from fastapi import BackgroundTasks, APIRouter, Form

router = APIRouter()


def print_log(msg: Optional[str]):
    time.sleep(1)
    print(msg)


@router.post('/tasks/log')
async def new_task(background_tasks: BackgroundTasks, msg: Optional[str] = Form(...)):
    background_tasks.add_task(print_log, msg)
    return {'msg': 'Task create success'}
