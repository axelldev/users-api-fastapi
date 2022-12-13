import db
from db import users
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path, Query, status, UploadFile
from models import UserResponse, User

app = FastAPI()


@app.get("/users", response_model=list[UserResponse], status_code=status.HTTP_200_OK, tags=["Users"])
async def get_users(
        limit: int = Query(
            10,
            gt=0,
            title="Limit",
            description="Number of users"
        ),
):
    """
    Get users

    This endpoint returns a list of users

    - **limit**: Number of users to return

    Returns a **list of users**
    """

    return users[:limit]


@app.get("/users/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK, tags=["Users"])
async def get_user_by_id(
        user_id: int = Path(
            gt=0,
            title="ID of the user",
            description="ID of the user"
        )
):
    """
    Get user by ID

    This endpoint returns a user by ID.

    - **user_id**: ID of the user to return

    Returns a **user**
    """

    filtered = list(filter(lambda user: user.id == user_id, users))

    if not filtered:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    return filtered[0]


@app.post("/users", status_code=status.HTTP_201_CREATED, tags=["Users", "Post"])
async def create_user(user: User):
    """
    Create user

    This endpoint creates a user.

    - **user**: User to create
    """

    db.users.append(user)


@app.post("/post-image", tags=["Post"])
def post_image(
        image: UploadFile
):
    return {
        "filename": image.filename,
        "format": image.content_type,
        "size": round(len(image.file.read()) / 1024, 2)
    }
