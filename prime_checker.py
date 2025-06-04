#!/usr/bin/env python3
"""Prime number checker utility."""

import argparse


def is_prime(n: int) -> bool:
    """Return True if ``n`` is a prime number, else False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to(limit: int):
    """Yield all primes up to ``limit`` inclusive."""
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num


def main() -> None:
    parser = argparse.ArgumentParser(description="Identify prime numbers")
    parser.add_argument(
        "number",
        type=int,
        help="Number to check for primality",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List all prime numbers up to the given number",
    )

    args = parser.parse_args()

    if args.list:
        primes = list(primes_up_to(args.number))
        print("Primes up to {}: {}".format(args.number, " ".join(map(str, primes))))
    else:
        if is_prime(args.number):
            print(f"{args.number} is prime")
        else:
            print(f"{args.number} is not prime")


if __name__ == "__main__":
    main()
