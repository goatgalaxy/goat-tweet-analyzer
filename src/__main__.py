import logging

from src.routes import routes

from loafer.managers import LoaferManager

logger = logging.getLogger(__name__)

logger.info("STARTED APLICATION - GOAT TWEETER ANALYZER")

manager = LoaferManager(routes=routes)
manager.run()