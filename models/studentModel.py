from pydantic import BaseModel, Field
from typing import Optional


class Student(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, description="Student name")
    marks: float = Field(..., ge=0, le=100, description="Marks must be between 0 and 100")
    course: str = Field(..., min_length=1, description="Course name")
