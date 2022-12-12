from pydantic import BaseModel, Field


class UserBase(BaseModel):
    id: int = Field(..., gt=0, title="ID of the user", description="ID of the user")
    name: str = Field(..., min_length=2, max_length=100, title="Name")
    age: int = Field(..., ge=18, le=120, title="Age")
    is_admin: bool = Field(False, title="Is Admin")


class User(UserBase):
    password: str = Field(..., min_length=8, max_length=100, title="Password")


class UserResponse(UserBase):
    pass
