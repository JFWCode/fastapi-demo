from typing import Optional

from fastapi import Depends, Cookie, status, Header
from fastapi.responses import JSONResponse
from fastapi import APIRouter

from models import UserOut, User

router = APIRouter()

def public_user(user_id: Optional[int]):
    if user_id:
        return True
    return False


def activate_user(user_id: Optional[int], check: bool = Depends(public_user)):
    if check and user_id == 1:
        return True
    return False


@router.get('/users/{user_id}')
async def get_user(user_id: int, user_agent: Optional[str] = Header(None)):
    return {'user': user_id, 'user_agent': user_agent}


@router.post('/users', response_model=UserOut)
async def create_users(user: User, ads_id: Optional[str] = Cookie(None)):
    data = user.dict()
    response = JSONResponse(data)
    response.set_cookie(key='ads_id', value=ads_id)
    return response


@router.get('/users/{user_id}/admin', status_code=status.HTTP_200_OK)
async def get_admin_user(check: bool = Depends(activate_user)):
    if check:
        return {'msg': 'Admin'}

    return {'msg': 'Not Admin'}
