from pydantic import BaseModel, Field


class GradeInput(BaseModel):
    bwl: float = Field(ge=1.0, le=6.0)
    mathe: float = Field(ge=1.0, le=6.0)
    deutsch: float = Field(ge=1.0, le=6.0)
    englisch: float = Field(ge=1.0, le=6.0)


class GradeEvaluation(BaseModel):
    average: float
    tutoring_subjects: list[str]
    needs_tutoring: bool


class HealthResponse(BaseModel):
    status: str
    database: str
