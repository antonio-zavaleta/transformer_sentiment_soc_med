import logging
import io

def log_message(message):
    print(f"[LOG] {message}")

def save_to_file(data, filename):
    with open(filename, 'w') as f:
        f.write(data)

def load_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def validate_data(data):
    if not data:
        raise ValueError("Data cannot be empty.")
    return True

def get_logger(level: int = logging.INFO,
               logger_name: str = "custom_logger",
               logger_format: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
               )-> tuple[io.StringIO, logging.Logger]:   
    """
    Creates and returns a custom logger with a specified logging level.
    Args:
        level (int): The logging level (e.g., logging.DEBUG, logging.INFO).
    Returns:
        tuple: A tuple containing:
            - log_stream (io.StringIO): The in-memory stream where log messages are written.
            - logger (logging.Logger): The configured logger instance.
    """

    log_stream = io.StringIO()
    logger = logging.getLogger("custom_logger")
    logger.setLevel(level)

    stream_handler = logging.StreamHandler(log_stream)
    stream_handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    
    return log_stream, logger