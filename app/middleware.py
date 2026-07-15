from typing import Callable
from time import perf_counter
import logging
from fastapi import Request


logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler("app.log", encoding="utf-8")],
                    )
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def logs_middleware(request: Request, call_next: Callable):
    start_time = perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        logger.exception("Unhandled exception")
        raise

    end_time = perf_counter()
    duration = end_time - start_time

    logger.info("method=%s path=%s status=%s duration=%.4fs",
                request.method,
                request.url.path,
                response.status_code,
                duration,
                )

    return response