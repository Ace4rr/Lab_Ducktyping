class ContractViolationError(TypeError):
    """Source doesn't match for contract (Protocol)"""

class InvalidTaskError(ValueError):
    """Too bad task (doesn't match to model)"""

    