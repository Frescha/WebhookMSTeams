import logging

from helpers.environments import config
from helpers.module_register import ModuleRegister
from app.webhook import app

if __name__ == '__main__':
    """
    This module starts the Webhook API server.
    """

    logging.basicConfig(filename=config.log_path, level=logging.DEBUG)
    logging.info("Starting WebHook API")
    app.run(host=config.host, port=config.port, debug=config.debug)
