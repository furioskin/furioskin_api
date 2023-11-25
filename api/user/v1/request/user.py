from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., description="Email")
    password: str = Field(..., description="Password")


class DoctorRequest(BaseModel):
    hospital: str = Field(..., description="hospital")