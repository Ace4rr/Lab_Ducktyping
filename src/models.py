from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class Task:
    """
    Base task model
    """
    id:str
    description:str 
    priority:str 
    status:str 
    created_at:datetime 

    def __validation__(self):
        if not self.id:
            raise ValueError("Task must be not empty")
        if not isinstance(self.priority,int):
            raise ValueError("Task prior must be not negative int")
        if not isinstance(self.created_at,datetime):
            raise ValueError("Task created_at must be datetime")
        
    @property
    def is_ready(self)->bool:
        """
        Is task ready for being completed check
        """
        return self.status.lower() in ("ready","todo","pending") and self.priority>0
    