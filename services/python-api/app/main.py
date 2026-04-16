from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.db import GradeEvaluationRecord, get_session, init_db
from app.schemas import GradeEvaluation, GradeInput, HealthResponse
from app.services import GradeEvaluationService

app = FastAPI(title="WebPy Template API", version="1.0.0")
service = GradeEvaluationService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    db_status = "ok"
    try:
        with get_session() as session:
            session.execute(text("SELECT 1"))
    except Exception:
        db_status = "unavailable"

    return HealthResponse(status="ok", database=db_status)


@app.post("/api/v1/grades/evaluate", response_model=GradeEvaluation)
def evaluate_grades(payload: GradeInput) -> GradeEvaluation:
    grades = payload.model_dump()
    result = service.evaluate(grades)

    record = GradeEvaluationRecord(
        bwl=grades["bwl"],
        mathe=grades["mathe"],
        deutsch=grades["deutsch"],
        englisch=grades["englisch"],
        average=result.average,
        tutoring_subjects=",".join(result.tutoring_subjects),
    )

    with get_session() as session:
        session.add(record)

    return GradeEvaluation(
        average=result.average,
        tutoring_subjects=result.tutoring_subjects,
        needs_tutoring=len(result.tutoring_subjects) > 0,
    )


@app.get("/api/v1/grades/evaluations")
def list_evaluations(limit: int = 20) -> list[dict[str, Any]]:
    safe_limit = max(1, min(limit, 100))
    with get_session() as session:
        rows = (
            session.query(GradeEvaluationRecord)
            .order_by(GradeEvaluationRecord.created_at.desc())
            .limit(safe_limit)
            .all()
        )

        return [
            {
                "id": row.id,
                "bwl": row.bwl,
                "mathe": row.mathe,
                "deutsch": row.deutsch,
                "englisch": row.englisch,
                "average": row.average,
                "tutoring_subjects": [s for s in row.tutoring_subjects.split(",") if s],
                "created_at": row.created_at.isoformat(),
            }
            for row in rows
        ]
