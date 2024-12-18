def print_fibonacci(length):
    """
    Prints the Fibonacci sequence up to the given length.

    Args:
        length (int): The number of Fibonacci numbers to print.
    """
    if length == 0:
        print("[]")  # Print an empty list for length 0
        return
    elif length == 1:
        print("[0]")  # Print a list with a single element for length 1
        return

    # Generate Fibonacci sequence for length > 1
    sequence = [0, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    print(sequence)
