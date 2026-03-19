from src.sources.generator_source import GeneratedTaskSource

def test_generator_src_returns_tasks():
    source=GeneratedTaskSource(count=3)
    tasks=list(source.get_tasks())
    assert len(tasks)==3
    assert tasks[0].id.startswith("gen-")