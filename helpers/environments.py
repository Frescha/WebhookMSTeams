from pathlib import Path
import os

class DevelopmentConfig:
    host = os.environ['APP_HOST']
    port = os.environ['APP_PORT']
    debug = os.environ['APP_DEBUG']
    log_path = os.environ['APP_LOG_PATH']
    LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()
    hookurl = "/api/v1/execution"

class ProductionConfig:
    host = os.environ['APP_HOST']
    port = os.environ['APP_PORT']
    debug = os.environ['APP_DEBUG']
    log_path = os.environ['APP_LOG_PATH']
    LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
    hookurl = "/api/v1/execution"

configurations = {
    "dev":  DevelopmentConfig,
    "prod": ProductionConfig }

environment = os.environ.get("BG_CONFIG", "dev")
config = configurations[environment]