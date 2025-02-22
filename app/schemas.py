from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
        
    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id : int
    owner: UserOut
    
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]