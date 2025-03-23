import logging.config
import os
from dotenv import load_dotenv


ENV_FILE = os.environ.get("ENV_FILE", ".env")
load_dotenv(ENV_FILE)

# LOG CONFIG
LOG_CONFIG = {
	"version": 1,
	"disable_existing_loggers": True,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "minimal": {"format": "[%(levelname)s]: %(message)s"},
    },
    "handlers": {
        "default": {
            "level": os.environ.get("LOG_LEVEL", "INFO"),
            "formatter": "minimal",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": int(os.getenv("LOG_FILE_MAX_SIZE") or 64 * 1024 * 1024),
            "backupCount": int(os.getenv("LOG_FILE_BACKUP_COUNT") or 3),
            "filename": os.getenv("LOG_FILE") or "./logs/execution.log",
        },
    },
    "loggers": {
        "": {
            "handlers": ["default", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
logging.config.dictConfig(LOG_CONFIG)

# SQL DATABASE
DATABASE_URI = os.environ.get(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432"
)

# AWS Credentials (Use it only if credentials cannot be passed implicitly)
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION") or "ap-southeast-2"

# OPENAI
OPENAI_KEY = os.environ.get("OPENAI_KEY")

# Add other settings below (Prefer using environment variable)
