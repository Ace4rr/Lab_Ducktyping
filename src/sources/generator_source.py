from __future__ import annotations
from typing import Iterable, Iterator
from datetime import datetime, timedelta
import itertools
import logging

from ..models import Task

logger = logging.getLogger(__name__)

class GeneratedTaskSource:
    """
    generates tasks
    """
    def __init__(self, count: int = 10, base_priority: int = 1):
        self.count = max(0, int(count))
        self.base_priority = int(base_priority)

    def get_tasks(self) -> Iterable[Task]:
        return self._gen()

    def _gen(self) -> Iterator[Task]:
        now = datetime.utcnow()
        for n in range(self.count):
            try:
                t = Task(
                    id=f"gen-{n}",
                    description=f"Generated task #{n}",
                    priority=self.base_priority + (n % 5),
                    status="ready" if (n % 2 == 0) else "pending",
                    created_at=now - timedelta(minutes=n),)
                yield t
            except Exception:
                logger.exception("Failed to generate task #%d", n)
                continue