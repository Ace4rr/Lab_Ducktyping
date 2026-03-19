from typing import Iterable, Protocol, runtime_checkable
from .models import Task

@runtime_checkable
class TaskSourceProtocol(Protocol):
    """
    Contract for task sources
    """
    def get_tasks(self)->Iterable[Task]:
        pass