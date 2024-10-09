import logging

import uvicorn
from fastapi import FastAPI
from auth.router import router as auth_router
from post_router.router import router as post_router
from logs.router import router as logs_router
import betterlogging as bl


def setup_logging():
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=log_level,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting server")


setup_logging()

app = FastAPI(title="Weather App")

app.include_router(post_router)
app.include_router(auth_router)
app.include_router(logs_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
