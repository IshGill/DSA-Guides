def calcEquation(self, equations, values, queries):
    # Step 1: Build the graph
    graph = collections.defaultdict(dict)
    # Default dict beacuse if a value DNE it won't throw an expection unlike normal dict
    for (num, denom), product in zip(equations, values):
        # zip(equations, values) = [([a, b], 2.0), ([b, c], 3.0)]
        graph[num][denom] = product
        ## dict[x][y] implies x is pointing to y. ie {'a': {'b': 2.0}} a is pointing to b.
        # Set the key as the num, denom and value as the product of the division in the defaultdict
        graph[denom][num] = 1.0 / product

    def dfs(numerator, denominator, visited):
        if numerator not in graph or denominator not in graph:
            return -1.0

        if denominator in graph[numerator]:
            return graph[numerator][denominator]
        # Recall that our dict is set up such that the numerator points to the deominator, hence if denominator is in the denominator it
        # is a key of the numerator so we can return that value.
        # ie {'a': {'b': 2.0}}, a is the numerator and b is the denominator. If the query was a/b we would ask "is b in a?" we can see it is hence we just return the value which is the product of a/b.

        for i in graph[numerator]:
            if i not in visited:
                visited.add(i)
                temp = dfs(i, denominator, visited)
                if temp == -1:
                    continue
                else:
                    return graph[numerator][i] * temp
        return -1

    result_list = []
    for numerator, denominator in queries:
        result_list.append(dfs(numerator, denominator, set()))
        # Pass the numerator and denominator of the query division to dfs where we will find the product.
    return result_list