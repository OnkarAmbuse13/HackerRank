"""
simple_hello_world.py

This module demonstrate a simple Hello World program
with custom exception handling.
"""

class HelloWorldError(Exception):
    """Custom Exception raised when printing Hello World fails."""
    
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        
    def __str__(self) -> str:
        return f"HelloWorldError: {self.message}"
    
def print_hello_World() -> None:
    """Print Hello World to the console.
    
    Raises:
        HelloWorldError: If printing fails
    """
    try:
        print("Hello, World!")
    except Exception as exc:
        raise HelloWorldError("Failed to print Hello World") from exc
    
def main() -> None:
    """Main entry of the script."""
    try:
        print_hello_World()
    except HelloWorldError as error:
        print(error)
        
if __name__ == "__main__":
    main()              