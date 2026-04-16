from dataclasses import dataclass


@dataclass
class EvaluationResult:
    average: float
    tutoring_subjects: list[str]


class GradeEvaluationService:
    """Encapsulates grade evaluation logic in a reusable service."""

    SUBJECTS = ("bwl", "mathe", "deutsch", "englisch")

    def evaluate(self, grades: dict[str, float]) -> EvaluationResult:
        values = [float(grades[name]) for name in self.SUBJECTS]
        average = round(sum(values) / len(values), 2)

        tutoring_subjects = [
            subject for subject in self.SUBJECTS if float(grades[subject]) > 4.0
        ]
        return EvaluationResult(average=average, tutoring_subjects=tutoring_subjects)
