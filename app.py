
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add(a, b):
    """Return a + b."""
    logger.info(f"Adding {a} + {b}")
    return a + b

def divide(a, b):
    """Return a / b."""
    logger.info(f"Dividing {a} / {b}")
    return a / b  # BUG if b = 0

def main():
    x, y = 10, 0
    print("Sum:", add(x, y))
    print("Quotient:", divide(x, y))

if __name__ == "__main__":
    main()
