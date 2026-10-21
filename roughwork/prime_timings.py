"""Time the five prime-generating approaches compared in
https://stackoverflow.com/a/39106237, plus the two changes suggested in
its comments.

AI use: this script was written by Claude (Opus 5.5,
via Claude Code) at my request. 

Run: python roughwork/prime_timings.py [n]
"""
import sys
import timeit


def trial_all(n):
    """Method 1: divide by every smaller number, never stopping early."""
    out = []
    for num in range(2, n + 1):
        is_prime = True
        for d in range(2, num):
            if num % d == 0:
                is_prime = False
        if is_prime:
            out.append(num)
    return out


def trial_stop_early(n):
    """Method 2: stop at the first divisor found."""
    return [num for num in range(2, n + 1)
            if all(num % d for d in range(2, num))]


def trial_to_root(n):
    """Method 3: only try divisors up to the square root."""
    return [num for num in range(2, n + 1)
            if all(num % d for d in range(2, int(num ** 0.5) + 1))]


def trial_odd_only(n):
    """Method 4: as method 3, but skip even numbers after 2."""
    return [2] + [num for num in range(3, n + 1, 2)
                  if all(num % d for d in range(2, int(num ** 0.5) + 1))]


def sieve(n):
    """Method 5: Sieve of Eratosthenes."""
    out = []
    flags = [True] * (n + 1)
    for p in range(2, n + 1):
        if flags[p]:
            out.append(p)
            for i in range(p, n + 1, p):
                flags[i] = False
    return out


def sieve_mod_check(n):
    """Method 5 with the extra `% 2` check the answer added later."""
    out = []
    flags = [True] * (n + 1)
    for p in range(2, n + 1):
        if flags[p] and flags[p] % 2 == 1:
            out.append(p)
            for i in range(p, n + 1, p):
                flags[i] = False
    return out


def sieve_odd_only(n):
    """Method 5 starting from [2] and looping over odd numbers only."""
    out = [2]
    flags = [True] * (n + 1)
    for p in range(3, n + 1, 2):
        if flags[p]:
            out.append(p)
            for i in range(p, n + 1, p):
                flags[i] = False
    return out


ALL_METHODS = [trial_all, trial_stop_early, trial_to_root, trial_odd_only,
               sieve, sieve_mod_check, sieve_odd_only]
SIEVES = [sieve, sieve_mod_check, sieve_odd_only]


def time_methods(methods, n, repeat):
    expected = sieve(n)
    print(f"n = {n:,} ({len(expected):,} primes), best of {repeat} runs")
    for method in methods:
        assert method(n) == expected, method.__name__
        best = min(timeit.repeat(lambda: method(n), number=1, repeat=repeat))
        print(f"  {method.__name__:<17} {best:9.4f} s")


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000
    time_methods(ALL_METHODS, n, repeat=3)
    print()
    time_methods(SIEVES, 1_000_000, repeat=5)
