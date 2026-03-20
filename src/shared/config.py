"""애플리케이션 설정 관리"""
from pydandtic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """환경변수 기반 애플리케이션 설정"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    # LLM API
    open_api_key: str
    open_base_url: str = "https://api.openai.com/v1"
    default_model: str = "gpt-5-nano"
    judge_model: str = "gpt-5-mini"

    # 벡터 DB
    chroma_host: str = "localhost"
    chroma_port: int = 8100

    # 평가
    eval_batch_size: int = 10
    eval_max_concurrency: int = 5

    # MLflow
    mlflow_tracking_uri: str = "http://localhost:5001"

settings = Settings()