import logging
import requests
import socket

from helpers.environments import config

class ModuleRegister:
    """
    Class for registering this service to webservice
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("ModuleRegister initialized")

        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(socket.gethostname())
        self.module = config.MODULE_TYPE
        self.port = config.port
    
    def check_webservice_status(self):
        """
        Check if webservice is up and running
        """
        self.logger.info("Checking if webservice is up and running")
        url = url = config.SCHEDULER_URL + "/api/v1/register"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.logger.info("Webservice is up and running")
            else:
                self.logger.error("Webservice is not up and running")
        except Exception as e:
            self.logger.error("Failed to check if webservice is up and running: %s", e)

    def register(self):
        """
        Register this service to webservice
        """
        self.logger.info("Registering this service to webservice")
        url = config.SCHEDULER_URL + "/api/v1/register"
        headers = {'Content-type': 'application/json'}
        data = {
            "hostname": self.hostname,
            "ip": self.ip,
            "port": self.port,
            "module": self.module,
            "name": "Dummy-Poller"
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                self.logger.info("Successfully registered this service to webservice")
            else:
                self.logger.error("Failed to register this service to webservice")
        except Exception as e:
            self.logger.error("Failed to register this service to webservice: %s", e)

    def unregister(self):
        """
        Unregister this service from webservice
        """
        self.logger.info("Unregistering this service from webservice")
        url = config.SCHEDULER_URL + "/api/v1/unregister"
        headers = {'Content-type': 'application/json'}
        data = {
            "hostname": socket.gethostname(),
            "ip": socket.gethostbyname(socket.gethostname()),
            "port": config.PORT,
            "module": config.MODULE_TYPE,
            "name": "Dummy-poller"
        }
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                self.logger.info("Successfully unregistered this service from webservice")
            else:
                self.logger.error("Failed to unregister this service from webservice")
        except Exception as e:
            self.logger.error("Failed to unregister this service from webservice: %s", e)

