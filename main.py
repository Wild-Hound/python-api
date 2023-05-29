from fastapi import FastAPI
from log.main import logCritical, logInfo

import model.urlModel as urlModel

from config.url_shortenerConfig import engine as url_shortenerEngine

from router.urlRouter import router as urlRouter


try:
    urlModel.Base.metadata.create_all(bind=url_shortenerEngine)
except:
    logCritical("Failed to migrate urlModel")
else:
    logInfo("Migrated urlModel")


try:
    app = FastAPI()
    app.include_router(urlRouter, prefix="/url_shortener", tags=["url"])
except:
    logCritical("Failed to start service")
else:
    logInfo("Service running on port 8000")
