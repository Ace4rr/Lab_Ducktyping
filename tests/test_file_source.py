from src.sources.file_source import FileTaskSource
import json 

def test_file_src_return_tasks(tmp_path):
    file_path=tmp_path/"tasks.json"
    data= [
        {
            "id": "1",
            "description": "api task",
            "priority": 5,
            "status": "ready",
            "created_at": "2024-01-01T12:00:00",
        }
    ]
    file_path.write_text(json.dumps(data))
    source=FileTaskSource(file_path)
    tasks= list(source.get_tasks())
    assert len(tasks)==1
    assert tasks[0].id == "1"
    assert tasks[0].priority == 5

def test_file_src_tasks_not_exist(tmp_path):
    file_path=tmp_path/"no_file.json"
    source=FileTaskSource(file_path)
    tasks=list(source.get_tasks())
    assert tasks==[]

def test_file_src_invalid_json(tmp_path):
    file_path=tmp_path/"bad.json"
    file_path.write_text("this is bad json")
    source=FileTaskSource(file_path)
    tasks=list(source.get_tasks())
    assert tasks==[]