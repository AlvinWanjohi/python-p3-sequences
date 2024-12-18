# sequences.py

def print_fibonacci(length):
    """
    Prints the Fibonacci sequence up to the given length.

    Args:
        length (int): The number of Fibonacci numbers to print.
    """
    if length == 0:
        print("[]")  # Output an empty list
    elif length == 1:
        print("[0]")  # Output a list with a single Fibonacci number
    else:
        # Generate Fibonacci sequence for length > 1
        sequence = [0, 1]
        for _ in range(2, length):
            sequence.append(sequence[-1] + sequence[-2])
        print(sequence)
