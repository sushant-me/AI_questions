"""
Create logging system.
"""

import logging
from logging.handlers import RotatingFileHandler

# Configure logging
def setup_logging():
    logger = logging.getLogger('example_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create handlers
    file_handler = RotatingFileHandler('example.log', maxBytes=1024*1024*5, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    
    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logging()
    logger.info("This is an info message")
    logger.error("This is an error message")