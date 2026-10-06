import time
import random
import matplotlib.pyplot as plt


# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def flawed_benchmark():
    """
    This benchmarking function contains several methodological errors.
    Rewrite this function to properly and fairly compare the two algorithms
    to demonstrate their scaling behavior.
    """
    
    # set up benchmarking parameters
    sizes = [500, 1000, 2000, 4000]
    repetitions = 5

    # set up empty lists to hold medians for plotting
    slow_medians = []
    fast_medians = []

    # set up user readability via clear direction and table headers
    print("Duplicate detection benchmark (median seconds; unique inputs)")
    print(f"{'n': >6} {'slow O(n^2)': >14} {'fast O(n)': >14}")

    # run the benchmark for each input size
    for n in sizes:
        # generate a list of unique integers of size n
        data = list(range(n))
        # create empty lists to hold the timing results for each algorithm
        slow_times = []
        fast_times = []

        # run each algorithm multiple times and record the execution time
        for _ in range(repetitions):
            # start a timer for the run of the slow algorithm
            start = time.perf_counter()
            # run the slow algorithm
            find_duplicates_slow(data)
            # save that time in a list as a float
            slow_times.append(time.perf_counter() - start)

            # start a timer for the run of the fast algorithm
            start = time.perf_counter()
            # run the fast algorithm
            find_duplicates_fast(data)
            # save that time in a list as a float
            fast_times.append(time.perf_counter() - start)

        # compute the median time for each algorithm and print the results
        slow_median = sorted(slow_times)[repetitions // 2]
        fast_median = sorted(fast_times)[repetitions // 2]
        print(f"{n:6d} {slow_median:14.6f} {fast_median:14.6f}")
        
        # append the medians to the plotting lists
        slow_medians.append(slow_median)
        fast_medians.append(fast_median)

    # plot the results
    plt.plot(sizes, slow_medians, marker="o", label="Slow O(n^2)")
    plt.plot(sizes, fast_medians, marker="o", label="Fast O(n)")
    plt.xlabel("Input size (n)")
    plt.ylabel("Median runtime (seconds)")
    plt.title("Duplicate Detection Benchmark")
    plt.legend()
    plt.tight_layout()
    plt.savefig("results3.png")
    plt.close()

    

if __name__ == "__main__":
    flawed_benchmark()