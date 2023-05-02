# DFA minimizat
def minimize_dfa(states, alphabet, transition_function, start_state, accepting_states):
    # Impartim starile in stari non-acceptoare si in stari acceptoare
    P = [states - accepting_states, accepting_states]
    # print(P)

    # Iteram pana cand partitionarea nu mai este posibila
    while True:
        # Cream un dictionar pentru a tine noile partitii(noul P)
        new_P = {}
        # print("Noul P", new_P)
        
        # Iteram fiecare partitie din P
        for partition in P:
            # Cream un dictionar pentru a tine noile partitii
            new_partition = {}
            # print(partition)

            # Iteram fiecare stare din partitie
            for state in partition:
                # print()
                # print(partition)
                # Cream un nou tuplu pentru a tine valorile tranzitiei
                transition_values = tuple(
                    transition_function[state][symbol] for symbol in alphabet
                )
                # print("Nod: ", state)
                # print()

                # Verificam daca valorile tranzitiei sunt in noua partitie
                if transition_values in new_partition:
                    # print("Tranzitia: ", transition_values)
                    new_partition[transition_values].append(state)
                    # print("Partitie_schimbata: ", new_partition)
                    # print()
                else:
                    # print("Tranzitia: ",transition_values)
                    new_partition[transition_values] = [state]
                    # print("Paritie_noua:", new_partition)

            # Adaugam noua partitie in noul dictionar
            for key in new_partition:
                # print()
                # print(key)
                # print("Noul P <<din for>>: ", new_P)
                aux=new_partition[key]
                for key_2 in new_partition:
                    if new_partition[key_2] != aux:
                        for key_3 in new_partition:
                            if (key_2[0] in new_partition[key] or key_2[1] in new_partition[key]) and (key[0] in new_partition[key_2] or key[1] in new_partition[key_2]):
                                print("Noduri echiv: ", new_partition[key], new_partition[key_2] )
                                break
                                
                            
                new_P[tuple(new_partition[key])] = new_partition[key]

        # Verificam daca partitionarea este completa
        if len(new_P) == len(P):
            # print(new_P)
            # print(P)
            break

        # Setam noua partitie
        P = list(new_P.values())
        # print("Noul_P a devenit P: ", P)

    # print(P)

    # Cream un nou dictionar pentru a tine tranzitiile automatului minimal
    new_transition_function = {}

    # Iteram fiecare partitie din P pentru a afisa tranzitiile din DFA minimal
    for partition in P:
        # Alegem starea reprezentativa a unei partiti (stari format din mai multe noduri din DFA complet)
        representative_state = partition[0]
        # print(representative_state)

        # Cream un nou dictionar pentru a tine tranzitiile stari reprezentative
        transition_dict = {}

        # Pentru fiecare simbol din alfabet
        for symbol in alphabet:
            # Luam valoarea tranzitiei pentru starea reprezentativa si simbolul 
            # print("Tranzitiile din DFA", transition_function)
            # print("Simbolul din alfabet: ",symbol)
            # print("Starea reprezentativa din nodurile in care se afla stari echivalente: ", representative_state)
            transition_value = transition_function[representative_state][symbol]
            # print(transition_value)

            # Gaseste partitia in care se afla valoarea tranzitiei
            for new_partition in P:
                # print("Partitia noua: ", new_partition)
                if transition_value in new_partition:
                    # print(transition_value)

                    # Setam starea reprezentativa pentru partitie( ex: am gasit valoarea in subgrupa [2,3] va )
                    new_representative_state = new_partition[0]
                    # print(new_representative_state)

                    # Adaugam tranzitia in noua functie de tranzitie
                    transition_dict[symbol] = new_representative_state
                    # print("Noua functie de tranzitie: " ,transition_dict[symbol])

                    # Iesim din loop daca valoarea tranzitiei se afla in partitie
                    break

        # Adaugam tranzitiile starii reprezentative in functie finala de tranzitie
        new_transition_function[representative_state] = transition_dict
        # print("Noua functie de tranzitie finala: ", new_transition_function)

    # Am creat o multime de tip set pentru a avea starile finale ale DFA minimal
    new_accepting_states = set()

    for partition in P:
        # Verificam daca partitia contine o stare acceptoare
        if any(state in accepting_states for state in partition):
            # Selectam starea reprezentativa din partitie(fiind prima)
            representative_state = partition[0]

            # Adaugam starile reprezentative in set-ul de stari acceptoare
            new_accepting_states.add(representative_state)

    # Returnam DFA minimizat
    return P, alphabet, new_transition_function, P[0][0], new_accepting_states

# Exemplu DFA
states = {0, 1, 2, 3, 4, 5}
alphabet = {'1', '0'}
transition_function = {
    0: {'0': 1, '1': 2},
    1: {'0': 0, '1': 3},
    2: {'0': 5, '1': 4},
    3: {'0': 5, '1': 4},
    4: {'0': 4, '1': 4},
    5: {'0': 5, '1': 4},
}
start_state = 0
accepting_states = {5}

new_states, new_alphabet, new_transition_function, new_start_state, new_accepting_states = minimize_dfa(states, alphabet, transition_function, start_state, accepting_states)

print()
print("DFA minimizat:")
print("Stari:", new_states)
print("Alfabet:", new_alphabet)
print("Starea initiala:", new_start_state)
print("Stari acceptoare:", new_accepting_states)
print("Tranzitii:", new_transition_function)