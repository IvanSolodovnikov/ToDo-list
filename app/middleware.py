import logging
from time import perf_counter
from typing import Callable

from fastapi import Request


logger = logging.getLogger("app.middleware")


async def logs_middleware(request: Request, call_next: Callable):
    start_time = perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        duration = perf_counter() - start_time

        logger.exception(
            "method=%s path=%s failed duration=%.4fs",
            request.method,
            request.url.path,
            duration,
        )
        raise

    duration = perf_counter() - start_time

    logger.info(
        "method=%s path=%s status=%s duration=%.4fs",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )

    return response
