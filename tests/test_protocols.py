from src.protocols import TaskSourceProtocol

class GoodSource:
    def get_tasks(self):
        return []
    
def test_protocol_good():
    source=GoodSource
    assert isinstance(source,TaskSourceProtocol)

class BadSource:
    pass 

def test_protocol_bad():
    source=BadSource
    assert not isinstance(source,TaskSourceProtocol)