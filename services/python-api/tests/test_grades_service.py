from app.services import GradeEvaluationService


def test_grade_evaluation_with_tutoring_need() -> None:
    service = GradeEvaluationService()

    result = service.evaluate(
        {"bwl": 4.5, "mathe": 2.5, "deutsch": 4.1, "englisch": 3.0}
    )

    assert result.average == 3.52
    assert result.tutoring_subjects == ["bwl", "deutsch"]


def test_grade_evaluation_without_tutoring_need() -> None:
    service = GradeEvaluationService()

    result = service.evaluate(
        {"bwl": 2.0, "mathe": 3.0, "deutsch": 2.5, "englisch": 3.5}
    )

    assert result.average == 2.75
    assert result.tutoring_subjects == []
