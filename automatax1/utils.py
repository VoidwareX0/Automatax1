"""Utility functions"""

import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automatax1')

def wait(seconds):
    """Wait helper"""
    time.sleep(seconds)

def debug(msg):
    """Debug logging"""
    logger.debug(msg)

def info(msg):
    """Info logging"""
    logger.info(msg)

def error(msg):
    """Error logging"""
    logger.error(msg)