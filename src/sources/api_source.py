from typing import Iterable, Iterator, Callable
from datetime import datetime
import logging

from ..models import Task

logger = logging.getLogger(__name__)


def _parse_datetime(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except Exception:
        raise ValueError(f"Invalid datetime format: {value!r}")
    

class ApiTaskSource:
    """
    Api tasks source
    gets fetcher() func and returns list[dict]
    """
    def __init__(self,fetcher:Callable[[],list[dict]]):
        if not callable(fetcher):
            raise ValueError("fetcher must be callable")
        self._fetcher=fetcher

    def get_tasks(self)->Iterable[Task]:
        try:
            raw=self._fetcher()
        except Exception as e:
            logger.exception(f"Api fetch failed as {e}")
            return [] 
        if not isinstance(raw,list):
            logger.error("Api fetcher must return a list of task dicts")

        def gen():
            for idx, item in enumerate(raw):
                try:
                    t = Task(
                        id=str(item["id"]),
                        description=str(item.get("description", "")),
                        priority=int(item.get("priority", 0)),
                        status=str(item.get("status", "") or ""),
                        created_at=_parse_datetime(item["created_at"]),
                    )
                    yield t
                except Exception as e:
                    logger.error("Skipping invalid task from API at index %d: %s", idx, e)
                    continue
        return gen()
                    