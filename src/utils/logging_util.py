import logging

def setup_logging(log_file='system.log'):
    """ Set up logging configuration """
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    return logging.getLogger()

# Example usage
if __name__ == "__main__":
    logger = setup_logging()
    logger.info('Logging setup complete.')
