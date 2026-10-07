class DomainError(Exception):
    def __init__(self, code: str, status: int, message: str = "") -> None:
        self.code = code
        self.status = status
        self.message = message or code
        super().__init__(self.message)
