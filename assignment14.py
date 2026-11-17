import logging

# Step 1: Configure logging
logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Step 2: Create a function to perform division
def divide_numbers(a, b):
    logging.debug("Division function started")

    try:
        logging.info("Performing division: %d / %d", a, b)

        result = a / b

        logging.info("Division completed successfully")
        logging.debug("Result calculated: %s", result)

        return result

    except ZeroDivisionError:
        logging.exception("Error occurred: Division by zero")
        return None

# Step 3: Call the function
print("Result:", divide_numbers(10, 2))
print("Result:", divide_numbers(10, 0))