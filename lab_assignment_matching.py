"""
Lab Assignment Matching
A preference-based, capacity-constrained matching algorithm.

Problem: assign students to labs based on (1) each student's ranked lab choices, (2) each lab's preference over students, and (3) a capacity for each lab.

This algorithm was designed and implemented entirely from scratch based only on the problem objective.
No existing solutions, online guides, or AI tools were used.

The algorithm processes students according to their preferences and uses each lab's ranking 
to decide which students are accepted when the lab reaches its capacity.
"""


def choice_append(choice, lapholder, studentlist):
    # Group students by which lab they picked
    chooseLap1, chooseLap2, chooseLap3 = [], [], []
    for s_i in studentlist:
        s_index = int(list(s_i)[1])
        if studentlist[s_i][choice] == 1:
            chooseLap1.append(s_index)
        elif studentlist[s_i][choice] == 2:
            chooseLap2.append(s_index)
        elif studentlist[s_i][choice] == 3:
            chooseLap3.append(s_index)
        lapholder.update({f'Choice: {choice+1}': [chooseLap1, chooseLap2, chooseLap3]})


def lap_select(lap, lapcap, lappref, lapholder):
    # assign students to labs by preference rank + displace current worst-ranked by a better-ranked applicant
    for choice, hold in lapholder.items():
        choice_index = int(list(choice)[8]) - 1
        retry = True
        while retry:
            for pref_index in range(3):
                break_again = False
                print(f"Choice {choice_index + 1}, Lap {pref_index + 1}: {hold[pref_index]}")
                to_remove = []
                rank_index = []
                for i in hold[pref_index]:
                    if i in lappref[pref_index]:
                        i_index = lappref[pref_index].index(i) + 1
                        rank_index.append(i_index)
                        #print(f"Student {i}: Lap like you! on rank {i_index}")
                    else:
                        to_remove.append(i)
                        #print(f"Student {i} :Sorry, lap don't like you")
                for student in to_remove:
                    hold[pref_index].remove(student)
                print("hold pref_index " + f"{hold[pref_index]}" + " Rank: " + f"{rank_index}" + ", respectively")

                for s in range(len(hold[pref_index]) - 1):
                    for j in range(len(hold[pref_index]) - s - 1):
                        if rank_index[j] < rank_index[j+1]:
                            hold[pref_index][j], hold[pref_index][j+1] = hold[pref_index][j+1], hold[pref_index][j]
                            rank_index[j], rank_index[j+1] = rank_index[j+1], rank_index[j]
                #print("Ranking student Lab want from least to most: "+ f"{hold[pref_index]}"+ " Rank: " + f"{rank_index}" + ", respectively\n")

                for k in range(len(hold[pref_index])):
                    new_student = hold[pref_index][k]
                    new_rank = rank_index[k]

                    if any(new_student in each_lap for each_lap in lap):
                        pass  # Already has a lap
                    elif len(lap[pref_index]) < lapcap[pref_index]:
                        lap[pref_index].append(new_student)
                        #print(f'Lap Member Iteration: {lap[0], lap[1], lap[2]}')
                    elif len(lap[pref_index]) >= lapcap[pref_index]:
                        #if new student has better rank (lower number), replace
                        worst_student = lap[pref_index][0]
                        worst_rank = lappref[pref_index].index(worst_student) + 1 if worst_student in lappref[pref_index] else float('inf')

                        if new_rank < worst_rank:
                            lap[pref_index].pop(0)
                            lap[pref_index].append(new_student)
                            retry = True
                            break_again = True
                            break
                if break_again:
                    break_again = False
                    #print(f'Lap Member Iteration: {lap[0], lap[1], lap[2]}\n')
                    break
                retry = False
                print(f'Lap Member Iteration: {lap[0], lap[1], lap[2]}\n')


def main():
    # Lab assignment slots (one list per lab)
    Lap = [[], [], []]

    # Lab capacities
    LapCap = [6, 6, 6]

    # Lab preferences over students (each lab's ranked list of student indices)
    LapPref = [
        [5, 3, 2, 6, 4],  # Lab 1
        [2, 6, 3, 5],     # Lab 2
        [2, 1, 3, 6, 4, 5],  # Lab 3
    ]

    # Student list with their ranked lab choices (1st, 2nd, 3rd; 0 = no choice)
    studentlist = {
        's1': [1, 0, 0], 's2': [1, 3, 0], 's3': [2, 1, 3],
        's4': [1, 2, 3], 's5': [3, 2, 1], 's6': [1, 2, 3],
    }

    # Build the per-choice grouping, then run the matching
    choice_holder = {}
    choice_append(0, choice_holder, studentlist)
    choice_append(1, choice_holder, studentlist)
    choice_append(2, choice_holder, studentlist)
    #print(f'{choice_holder}\n')
    lap_select(Lap, LapCap, LapPref, choice_holder)

    print("\nFinal assignment:")
    for idx, members in enumerate(Lap):
        print(f"  Lab {idx + 1}: {members}")


if __name__ == "__main__":
    main()