"""Check whether a user-provided integer is prime."""


def is_prime(number: int) -> bool:
    """Return True when number is a prime number."""
    if number <= 1:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def main() -> None:
    """Prompt for a number and print whether it is prime."""
    number = int(input("Enter a number: "))

    if is_prime(number):
        print("It is Prime Number")
    else:
        print("Not a Prime Number")


if __name__ == "__main__":
    main()
