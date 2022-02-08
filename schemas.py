from typing import Optional
from pydantic import BaseModel

class TodoBody(BaseModel):
  title: str
  description: str


class Todo(BaseModel):
  id: str
  title: str
  description: str
  

class SuccessMSG(BaseModel):
  message: str


class UserBody(BaseModel):
  email: str
  password: str


class UserInfo(BaseModel):
  id: Optional[str] = None
  email: str