from pydantic import BaseModel, EmailStr

class userRegisterSchema(BaseModel):
    firstname: String
    lastname: String
    username: String
    email: EmailStr
    paassword: String