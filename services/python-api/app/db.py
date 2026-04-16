import os
from contextlib import contextmanager
from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


def _build_database_url() -> str:
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    user = os.getenv("DB_USER", "appuser")
    password = os.getenv("DB_PASSWORD", "apppassword")
    name = os.getenv("DB_NAME", "appdb")
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}"


DATABASE_URL = _build_database_url()
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class GradeEvaluationRecord(Base):
    __tablename__ = "grade_evaluations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    bwl: Mapped[float] = mapped_column(Float)
    mathe: Mapped[float] = mapped_column(Float)
    deutsch: Mapped[float] = mapped_column(Float)
    englisch: Mapped[float] = mapped_column(Float)
    average: Mapped[float] = mapped_column(Float)
    tutoring_subjects: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


@contextmanager
def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
