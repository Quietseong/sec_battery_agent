"""커스텀 예외 클래스"""

class PlatformError(Exception):
    """기본 예외 설정"""


class EvalError(PlatformError):
    """평가 관련 에러"""
    
    def __init__(self, message: str, item_id: str | None = None) -> None:
        self.item_id = item_id
        super().__init__(message)


class LLMError(PlatformError):
    """LLM API 관련 에러"""
    
    def __init__(self, message: str, model: str | None = None, status_code: int | None = None) -> None:
        self.model = model
        self.status_code = status_code
        super().__init__(messagse)


class DataError(PlatformError):
    """데이터 관련 에러(로딩, 파싱, 검증)"""