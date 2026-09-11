"""
Genetic Algorithm for MaxOnes Problem

This script uses a genetic algorithm to solve the MaxOnes problem,
where the goal is to maximize the number of 1s in a binary string of length 100.

The algorithm evolves a population of binary strings through multiple generations using selection, crossover, and mutation. 
Different population sizes and mutation rates are tested, and the fitness over generations is plotted for each case.
"""

import random
import copy
import matplotlib.pyplot as plt

# Main Loop for Cases
def elite(pop_size, seque):
    elit = 0
    elit_str = -1
    all_gen = []
    for i in range(1, pop_size + 1):
        if elit_str < seque[i][1]:
            elit = i
            elit_str = seque[i][1]
            all_gen.append(elit_str)
    mean = sum(all_gen)/len(all_gen)
    return elit, elit_str, mean

# Parents
def parents(pop_size, seque):
    # Choose Father
    f_1 = random.randint(1, pop_size)
    f_2 = random.randint(1, pop_size)
    while f_2 == f_1:
        f_2 = random.randint(1, pop_size)
    
    if seque[f_1][1] > seque[f_2][1]:
        f = f_1
    else:
        f = f_2

    # Choose Mother
    m_1 = random.randint(1, pop_size)
    m_2 = random.randint(1, pop_size)
    while m_2 == m_1:
        m_2 = random.randint(1, pop_size)
        
    if seque[m_1][1] > seque[m_2][1]:
        m = m_1
    else:
        m = m_2

    return f, m

# Offspring
def crossover(seque, father, mother, mut_prob):
    off_gene_list = []
    
    father_gene = seque[father][0]
    mother_gene = seque[mother][0]

    for i in range(100):
        if father_gene[i] == mother_gene[i]:
            off_gene_list.append(father_gene[i])
        else:
            if random.randint(0, 1) == 0:
                off_gene_list.append(father_gene[i])
            else:
                off_gene_list.append(mother_gene[i])
    
    # Mutation
    if random.random() < mut_prob:
        if off_gene_list[-1] == '1':
            off_gene_list[-1] = '0'
        else:
            off_gene_list[-1] = '1'
            
    return "".join(off_gene_list)

def main():
    seque = {}

    cases = [
        {'population': 10, 'mutation_rate': 0.05, 'name': 'Pop=10, Mut=0.05'},
        {'population': 100, 'mutation_rate': 0.05, 'name': 'Pop=100, Mut=0.05'},
        {'population': 10, 'mutation_rate': 0.3, 'name': 'Pop=10, Mut=0.30'},
        {'population': 100, 'mutation_rate': 0.3, 'name': 'Pop=100, Mut=0.30'},
    ]

    all_results = {}

    for case in cases:
        pop_size = case['population']
        mut_prob = case['mutation_rate']
        case_name = case['name']
        
        # Initialize population for this case
        seque = {}
        print(f'\n--- Case: {case_name}')
        print('--- Generation 0')
        for i in range(1, pop_size + 1):
            m = str()
            strength = 0
            seque.update({i:[]})
            for j in range(100):
                seque[i].append(random.randint(0,1))

            m = "".join(map(str, seque[i]))
            strength = m.count('1')
            
            seque.update({i:[m, strength]})
            print(f'{i} : {seque[i]}')

        max_gen = []
        mean_gen = []
        elit, maximum, mean = elite(pop_size, seque)
        max_gen.append(maximum)
        mean_gen.append(mean)

        for generation in range(10):
            seque_gen = copy.deepcopy(seque) 
            
            seque_gen[1] = seque[elit]
            
            for gen_member in range(2, pop_size + 1):
                fath, moth = parents(pop_size, seque)
                new_gene = crossover(seque, fath, moth, mut_prob)
                
                new_strength = new_gene.count('1')
                
                seque_gen[gen_member] = [new_gene, new_strength]

            seque = seque_gen
            
            print(f'----- Generation {generation + 1}')
            for j in range(1, pop_size + 1):
                print(f'{j} : {seque[j]}')

            elit, maximum, mean = elite(pop_size, seque)
            max_gen.append(maximum)
            mean_gen.append(mean)

        print(f'Max: {max_gen}')
        print(f'Mean: {mean_gen}')
        
        all_results[case_name] = {'max': max_gen, 'mean': mean_gen}

    # Plot Results
    plt.figure(figsize=(12, 6))

    colors = ['blue', 'orange', 'green', 'red']

    for idx, (case_name, results) in enumerate(all_results.items()):
        plt.plot(range(11), results['max'], label=f'{case_name} - Max', 
                color=colors[idx], linestyle='-', marker='o')
        plt.plot(range(11), results['mean'], label=f'{case_name} - Mean', 
                color=colors[idx], linestyle='--', marker='s')

    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Evolution of Fitness Over Generations - All Cases')
    plt.legend(loc='best')
    plt.grid(True)
    plt.xlim(0, 10)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()