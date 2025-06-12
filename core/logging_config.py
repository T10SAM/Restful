import logging
import sys

logger = logging.getLogger("api_logger")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Formatação estruturada (JSON-like ou texto)
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)