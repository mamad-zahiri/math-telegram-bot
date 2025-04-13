from jdatetime import datetime as jdatetime

from src.db.models import Competition


def create_competition(
    start: jdatetime,
    end: jdatetime,
    score_threshold: int,
) -> Competition:
    return Competition.create(
        start=start.togregorian(),
        end=end.togregorian(),
        score_threshold=score_threshold,
    )
