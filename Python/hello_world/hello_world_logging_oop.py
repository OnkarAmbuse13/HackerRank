"""

hello_world_logging_oop.py

This module demonstrates the object-oriented Hello World program 
with logging, custom exception and oop best practices
"""
import logging


class HelloWorldError(Exception):
    """Custom exception raised when printing Hello World fails."""
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
    
    def __str__(self):
        return f"HelloWorldError: {self.message}"


class HelloWorldPrinter:
    """Encapsulate the behavior of printing Hello World."""
    
    def __init__(self, message: str = "Hello, World!") -> None:
        self.message = message
        
    def print_message(self) -> None:
        """Print the Hello World message.
        
        Raises:
            HelloWorldError: If printing fails.
        """
        try:
            print(self.message)
        except Exception as exc:
            raise HelloWorldError("Failed to print message") from exc
        

class Application:
    """Main Application class to run the Hello World Program."""
    
    def __init__(self, printer: HelloWorldPrinter, logger: logging.Logger) -> None:
        self.printer = printer
        self.logger = logger
    
    def run(self) -> None:
        """Run the application and handle the Exceptions."""
        try:
            self.logger.debug("Application started.")
            self.printer.print_message()
            self.logger.info("Message printed successfully.")
        except HelloWorldError as error:
            self.logger.error("Application error occurred: %s", error, exc_info=True)
        finally:
            self.logger.debug("Application finished.")
    
def configure_logger() -> logging.Logger:
    """Configure and return a logger instance."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(__name__)

def main() -> None:
    """Main entry point of the script."""
    logger = configure_logger()
    printer = HelloWorldPrinter()
    app = Application(printer, logger)
    app.run()


if __name__ == "__main__":
    main()