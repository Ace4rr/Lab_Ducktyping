from src.models import Task
from datetime import datetime

def test_task_is_ready_test():
    task=Task(
        id="1",
        description="idks",
        priority=3,
        status="ready",
        created_at=datetime.now()
    )
    result=task.is_ready
    assert result is True

def test_validation_empty():
    task=Task(
        id="",
        description="idks",
        priority=3,
        status="ready",
        created_at=datetime.now()
    )
    assert ValueError

def test_validation_priority():
    task=Task(
        id="",
        description="idks",
        priority="23",
        status="ready",
        created_at=datetime.now()
    )
    assert ValueError

def test_validation_datetime():
    task=Task(
        id="",
        description="idks",
        priority=3,
        status="ready",
        created_at=42
    )
    assert ValueError

import pytest

def test_validation_empty_id():
    task = Task(
        id="",
        description="idks",
        priority=3,
        status="ready",
        created_at=datetime.now()
    )
    with pytest.raises(ValueError):
        task.__validation__()

def test_validation_priority_not_int():
    task = Task(
        id="1",
        description="idks",
        priority="23",
        status="ready",
        created_at=datetime.now()
    )
    with pytest.raises(ValueError):
        task.__validation__()

