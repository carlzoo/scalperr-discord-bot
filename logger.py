import logging
import sys

logger = logging.getLogger('scalperr_discord_bot')
logger.setLevel(logging.DEBUG)
console_log_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] %(name)s - %(message)s')
console_log_handler.setFormatter(formatter)
console_log_handler.setLevel(logging.DEBUG)
logger.addHandler(console_log_handler)
