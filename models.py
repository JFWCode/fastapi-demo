from enum import Enum
from pydantic import BaseModel

class Gender(str, Enum):
    man = "man"
    women = "women"


class User(BaseModel):
    name: str
    age: int
    gender: Gender


class UserOut(BaseModel):
    name: str
    age: int
    gender: Gender
    password: str = '*****'