import db
from db import users
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path, Query, status, UploadFile
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
    filtered = list(filter(lambda user: user.id == user_id, users))

    if not filtered:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    return filtered[0]


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    db.users.append(user)


@app.post("/post-image")
def post_image(
        image: UploadFile
):
    return {
        "filename": image.filename,
        "format": image.content_type,
        "size": round(len(image.file.read()) / 1024, 2)
    }
