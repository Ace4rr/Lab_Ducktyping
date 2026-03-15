from typing import Iterable, Iterator
import logging 

from .protocols import TaskSourceProtocol
from .models import Task
from .exceptions import ContractViolationError, InvalidTaskError

logger=logging.getLogger(__name__)

class TaskReceiver():
    """
    Receives TaskSourceProtocol objects and returns iterator of right Task-type objects
    """
    def __init__(self,source: TaskSourceProtocol):
        """Checking contract"""
        if not isinstance(source,TaskSourceProtocol):
            raise ContractViolationError
        self._source=source
    def load_tasks(self)->Iterator[Task]:
        """
        Iterating all objects. Validating all obj and skipping negative
        """
        for maybe_task in self._source.get_tasks():
            try:
                task=self._validate_task(maybe_task)
            except InvalidTaskError as e:
                logger.error(f"Invalid task,{e}")
                continue
            yield task
    
    @staticmethod
    def _validate_task(obj)->Task:
        if not isinstance(obj,Task):
            raise InvalidTaskError("Item isnt isinstance")
        if obj.priority<0:
            raise InvalidTaskError("Item's priority is below zero")
        return obj
    