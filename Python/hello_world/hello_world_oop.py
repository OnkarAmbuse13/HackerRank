"""

hello_world_oop.py

This module demonstrates an object-oriented Hello World program
with custom exception handling. 
"""


class HelloWorldError(Exception):
    def __init__(self, message: str) -> None:
        super().__init___(message)
        self.message = message
        
    def __str__(self) -> str:
        return f"HelloWorldError: {self.message}"
    

class HelloWorldPrinter:
    """Encapsulate the behavior of printing Hello World."""
    def __init__(self, message: str = "Hello, World!") -> None:
        self.message = message
        

    def print_message(self) -> None:
        """Print Hello, World! Message.
        
        Raises:
            HelloWorldError: If printing fails.
        """
        
        try:
            print(self.message)
        except Exception as exc:
            raise HelloWorldError("Failed to print message") from exc
        

class Application:
    """Main Application class to run the Hello World program."""
    
    def __init__(self, printer: HelloWorldPrinter) -> None:
        self.printer = printer
    
    def run(self) -> None:
        """Run the application and handle the exceptions"""
        try:
            self.printer.print_message()
        except HelloWorldError as error:
            print(error)
            
    
def main() -> None:
    """Main entry of the script."""
    printer = HelloWorldPrinter()
    app = Application(printer)
    app.run()
    
if __name__ == "__main__":
    main()
