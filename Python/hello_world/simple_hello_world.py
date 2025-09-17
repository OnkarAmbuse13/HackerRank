"""
simple_hello_world.py

This program is used to log hello worlds message to console

"""
import logging
def config_logger() -> logging:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(message)s",
    )
    return logging.getLogger(__name__)
    
def main() -> None:
    logger = config_logger()
    logger.info("hello world")
    
if __name__ == '__main__':
    main()
    
    
