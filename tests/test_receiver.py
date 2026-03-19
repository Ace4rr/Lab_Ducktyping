from src.receiver import TaskReceiver
from datetime import datetime
from src.models import Task

class FakeSource:
    
    def get_tasks(self):
        return [
            Task(
                id="1",
                description="ok",
                priority=1,
                status="ready",
                created_at=datetime.now()
            )
        ]

def test_receiver_load_tasks():
    receiver=TaskReceiver(FakeSource())
    tasks=list(receiver.load_tasks())
    assert len(tasks)==1
    assert tasks[0].id=="1"