from pydantic import BaseModel, Field


class UserBase(BaseModel):
    id: int = Field(..., gt=0, title="ID of the user", description="ID of the user", example=1)
    name: str = Field(..., min_length=2, max_length=100, title="Name", example="John Doe")
    age: int = Field(..., ge=18, le=120, title="Age", example=18)
    is_admin: bool = Field(False, title="Is Admin", example=False)


class User(UserBase):
    password: str = Field(..., min_length=8, max_length=100, title="Password")


class UserResponse(UserBase):
    pass
