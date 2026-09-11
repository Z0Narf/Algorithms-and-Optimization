# Algorithms-and-Optimization

This is a collection of optimization and matching algorithms developed in Python as part of a programming course at the Institute of Science Tokyo.

The repository focuses on implementing the algorithms and testing how they behave under different conditions.

## Overview

This repository contains several Python scripts covering gradient descent, genetic algorithms, and preference-based matching. Each script is self-contained and includes the implementation, the main execution code, and visualizations or results where relevant.

The main focus is on the algorithms themselves rather than long written analysis. The scripts explore numerical optimization, evolutionary computation, and matching problems.

## Contents

### `lab_assignment_matching.py` (Preference-Based Matching)

Assigns students to labs based on each student's ranked lab choices, each lab's preference over students, and the capacity of each lab.

This one is my main *highlights* of the repository. The algorithm was designed and implemented from scratch using only the problem objective. I did not use existing solutions, search for the answer, or use AI tools. The professor gave us time to figure out the algorithm ourselves before introducing the standard solution, and I was able to complete my own version during class.

Afterward, I learned that the problem is closely related to the **Gale–Shapley stable matching problem**. Gale and Shapley's work on stable matching became part of the research recognized by the **2012 Nobel Prize in Economic Sciences**, awarded to Lloyd Shapley and Alvin Roth for their work on stable allocations and market design.

My implementation reaches the same type of matching problem through my own approach, using preference rankings and a capacity-based replacement rule, where a higher-ranked student can replace the lowest-ranked student when a lab is already full.

### `gradient_descent_contour.py` (Gradient Descent)

Visualizes the trajectory of gradient descent on the contour plot of a non-convex function,

`f(x1, x2) = 2*cos(2^x1 - x2^2 + 1) + exp((x1^2 + x2^2)/6)`

The gradient is calculated numerically, and different learning rates and starting points are compared to see how they affect the optimization process.

### `genetic_algorithm_maxones.py` (Genetic Algorithm for MaxOnes)

Uses a genetic algorithm to solve the MaxOnes problem, where the goal is to maximize the number of `1`s in a binary string of length 100.

The algorithm uses tournament selection, uniform crossover, mutation, and elitism. Different population sizes and mutation rates are tested, and the fitness over generations is plotted for each case.

### `genetic_algorithm_shopping.py` (Genetic Algorithm for Shopping)

Uses a genetic algorithm to solve a shopping problem, where the goal is to maximize satisfaction while staying within a given budget.

The model uses genetic algorithm operations to search for a suitable combination of items while handling solutions that exceed the budget.

## Concepts & tools demonstrated

- **Optimization:** gradient descent with numerical differentiation, learning-rate effects, non-convex functions
- **Evolutionary computation:** genetic algorithms, selection, crossover, mutation, elitism, and constrained optimization
- **Matching / combinatorics:** preference-based assignment with capacity constraints; independent derivation of a stable-matching-style algorithm
- **Python:** NumPy, Matplotlib, functions

## Running locally

```bash
git clone https://github.com/Z0Narf/Algorithms-and-Optimization.git
cd Algorithms-and-Optimization
pip install -r requirements.txt
python lab_assignment_matching.py
```

The other scripts can be run in the same way by replacing the filename.

## License

Shared under the MIT License ([LICENSE](LICENSE)). Problem statements are paraphrased from course material and belong to the original instructors.