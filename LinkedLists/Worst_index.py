def worst_index(size, values):
    new_table = HashTable(size)
    [new_table.put(i) for i in values]
    probe_number = [new_table.probe(i) for i in range(size)]
    return [i for i in range(len(probe_number)) if probe_number[i] == max(probe_number)]