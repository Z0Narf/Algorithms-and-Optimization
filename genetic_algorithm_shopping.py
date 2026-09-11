"""
Genetic Algorithm for Shopping Problem

This script uses a genetic algorithm to solve the shopping problem,
where the goal is to maximize satisfaction while staying within a given budget.
"""

import random
import copy
import matplotlib.pyplot as plt

# Fitness evaluation
def fitness(BUDGET, gene, items):
    total_price = 0
    total_satisfaction = 0

    for bit, (_, price, sat) in zip(gene, items):
        if bit == '1':
            total_price += price
            total_satisfaction += sat

    if total_price > BUDGET:
        return 0
    return total_satisfaction



# Elite selection
def elite(pop_size, seque):
    elit = 1
    elit_fit = seque[1][1]
    all_fit = []

    for i in range(1, pop_size + 1):
        all_fit.append(seque[i][1])
        if seque[i][1] > elit_fit:
            elit = i
            elit_fit = seque[i][1]

    mean = sum(all_fit) / len(all_fit)
    return elit, elit_fit, mean



# Parent selection (tournament)
def parents(pop_size, seque):
    def tournament():
        a, b = random.sample(range(1, pop_size + 1), 2)
        return a if seque[a][1] > seque[b][1] else b

    return tournament(), tournament()



# Crossover + mutation
def crossover(seque, father, mother, mut_prob, GENE_LENGTH):
    father_gene = seque[father][0]
    mother_gene = seque[mother][0]

    offspring = []
    for i in range(GENE_LENGTH):
        offspring.append(father_gene[i] if random.random() < 0.5 else mother_gene[i])

    # Mutation: flip one random bit
    if random.random() < mut_prob:
        idx = random.randint(0, GENE_LENGTH - 1)
        offspring[idx] = '0' if offspring[idx] == '1' else '1'

    return "".join(offspring)


def main():
    # Shopping problem definition
    items = [
        ("A1", 50, 1), ("A2", 50, 1),
        ("B1", 100, 2), ("B2", 100, 2), ("B3", 100, 2),
        ("C", 200, 3),
        ("D1", 300, 5), ("D2", 300, 5),
        ("E", 500, 7),
        ("F", 600, 9),
    ]

    GENE_LENGTH = len(items)
    BUDGET = 1000


    # Main GA loop (single case)
    pop_size = 100
    mut_prob = 0.1
    generations = 10

    seque = {}

    print('--- Generation 0 ---')
    for i in range(1, pop_size + 1):
        gene = "".join(str(random.randint(0, 1)) for _ in range(GENE_LENGTH))
        fit = fitness(BUDGET, gene, items)
        seque[i] = [gene, fit]
        print(i, seque[i])

    max_gen = []
    mean_gen = []

    elit, maximum, mean = elite(pop_size, seque)
    max_gen.append(maximum)
    mean_gen.append(mean)

    for gen in range(generations):
        seque_new = copy.deepcopy(seque)
        seque_new[1] = seque[elit]  # elitism

        for i in range(2, pop_size + 1):
            f, m = parents(pop_size, seque)
            gene = crossover(seque, f, m, mut_prob, GENE_LENGTH)
            seque_new[i] = [gene, fitness(BUDGET, gene, items)]

        seque = seque_new

        print(f'--- Generation {gen + 1} ---')
        for i in range(1, pop_size + 1):
            print(i, seque[i])

        elit, maximum, mean = elite(pop_size, seque)
        max_gen.append(maximum)
        mean_gen.append(mean)



    # Plot
    plt.plot(range(generations + 1), max_gen, marker='o', label='Max Satisfaction')
    plt.plot(range(generations + 1), mean_gen, marker='s', linestyle='--', label='Mean Satisfaction')
    plt.xlabel('Generation')
    plt.ylabel('Satisfaction')
    plt.title('GA Shopping Optimization (Budget ≤ 1000)')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()