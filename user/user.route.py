from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session  #query and write in database
from user.model import User, UserRole
from schemas.user.schema import userRegisterSchema

router = APIRouter (prefix="/user")

@router.post("/add")

def add_user(user_data: userRegisterSchema, db: Session = Depends(get_db))
return{"message": "User added"}

if db.query(User).filter(User.email == user_data.email).first():
    return{"message": "Email already exists"}
    print(user_data)

    #create user
    new-user = User(
        first_name = user_data.firstname,
        last_name = user_data.lastname,
        username = user_data.username,
        email=user_data.email,
        password = user_data.password,
        role=UserRole.User
    )

db.add(newUser)
db.commit()
db.refresh(new_user)

return{
    "message": "User added successfully",
    "user":{
        "id": new_user.id
        "first_name": new_user.firstname,
        "last_name": new_user.lastname,
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role.value


    }
}
