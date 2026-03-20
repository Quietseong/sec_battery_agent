"""  평가 파이프라인 데이터 모델 """

from datetime import datetime
from pydantic import BaseModel, Field

class QAItem(BaseModel):
    """QA Pair"""
    
    id: str
    question: str
    reference_answer: str
    context: str = ""
    metadata: dict[str, str] = Field(default_factory=dict)


class EvalResult(BaseModel):
    """단일 평가 결과"""

    item_id: str
    question: str
    reference_answer: str
    generated_answer: str
    score: float = Field(ge=0.0, le=5.0)
    reasoning: str = ""
    latenccy_ms: float = 0.0


class EvalReport(BaseModel):
    """평가 리포트"""

    experiment_name: str
    model_name: str
    timestamp: datetime = Field(default_factory=datetime.now)
    total_items: int
    avg_score: float
    median_score: float
    min_score: float
    max_score: float
    results: list[EvalResult]