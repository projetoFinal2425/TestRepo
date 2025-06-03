import random
import statistics

def generate_random_numbers(count=10, lower_bound=1, upper_bound=100):
    """Generate a list of random integers."""
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]

def calculate_statistics(numbers):
    """Calculate and return mean, median, and standard deviation."""
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    stdev = statistics.stdev(numbers)
    return mean, median, stdev

def main():
    print("Generating random numbers...")
    numbers = generate_random_numbers()
    print(f"Random Numbers: {numbers}")

    mean, median, stdev = calculate_statistics(numbers)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {stdev:.2f}")

if __name__ == "__main__":
    main()