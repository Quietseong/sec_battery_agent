"""구조화된 로깅 설정"""

import logging
import sys
from pathlib import Path

def setup_logger(
    name: str,
    level: int = logging.INFO,
    lof_file: Path | None = None,
) -> logging.Logger:
    """파일 + 콘솔 동시 출력 logger 설정"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    if lof_file:
        log_file.parent.mkdir(parents=True, exists_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger