# CMPSC 202 - Midterm Programming Assignment

Name: Ainslee Plesko

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

## Methodological Errors Fixed:
The original benchmark:
- only used one input size which doesn't show how the algorithm grows over time
- tested two sets of randomly generated data - the time comparison is not fair if the data tested is not the same, & there is potential for duplicate values which may return early
- times around the function rather than the algorithm call
- only runs once per algorithm, which will not account for cutting out background processes like repeition meadian testing will

## How I Fixed Them:
The new benchmark:
- tests multiple sizes (eg, 500, 1000, 2000, 4000)
- sets up a no-duplicate dataset (eg, `data = list(range(n)))`)
- uses the same dataset for both algorithms
- made the timing more precise (eg, only around the algorithm calls, uses `time.perf_counter()`)
- runs each alogorithm multiple times and takes the median to reduce background noise from the analysis
- more readable because of data printing in a table


2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.
