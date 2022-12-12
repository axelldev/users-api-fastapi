import db
from db import users
from fastapi import FastAPI
from fastapi import Path, Query, status
from models import UserResponse, User

app = FastAPI()


@app.get("/users", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
async def get_users(
        limit: int = Query(
            10,
            gt=0,
            title="Limit",
            description="Number of users"
        ),
):
    """Gets all the users"""

    return users[:limit]


@app.get("/users/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user_by_id(
        user_id: int = Path(
            gt=0,
            title="ID of the user",
            description="ID of the user"
        )
):
    """Gets a user by the ID"""
    user = None

    for u in users:
        if u.id == user_id:
            user = u

    return user


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    db.users.append(user)

