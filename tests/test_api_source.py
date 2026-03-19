from src.sources.api_source import ApiTaskSource
from datetime import datetime

def test_api_src_return_tasks():
    def fetcher():
        return [
            {
                "id": "1",
                "description": "api task",
                "priority": 5,
                "status": "ready",
                "created_at": "2024-01-01T12:00:00",
            }
        ]
    
    source=ApiTaskSource(fetcher)
    tasks=list(source.get_tasks())
    assert tasks[0].id=="1"
    assert tasks[0].priority==5

def test_api_src_return_fetch_error():
    def fetcher():
        raise RuntimeError("Api down")
    source=ApiTaskSource(fetcher)
    tasks=list(source.get_tasks())
    assert tasks==[]

def test_api_skip_invalid_task():
    def fetcher():
        return [
            {
                "id": "1",
                "description": "ok",
                "priority": 1,
                "status": "ready",
                "created_at": "2024-01-01T12:00:00",
            },
            {
                "id": "bad",
                "description": "wrong",
                "priority": 1,
                "status": "ready",
                "created_at": "bad-date",
            },
        ]
    
    source=ApiTaskSource(fetcher)
    tasks=list(source.get_tasks())
    assert tasks[0].id=="1"
