def eliminate_ambiguity():
    print("\n--- Ambiguity Elimination (Expression Grammar) ---")
    grammar = {
        "E": ["E + T", "T"],
        "T": ["T * F", "F"],
        "F": ["id"]
    }
    for nt, prods in grammar.items():
        print(f"{nt} -> {' | '.join(prods)}")


# --------------------------------
# Left Recursion Elimination
# --------------------------------
def eliminate_left_recursion(non_terminal, productions):
    alpha = []
    beta = []

    for prod in productions:
        if prod.startswith(non_terminal):
            alpha.append(prod[len(non_terminal):])
        else:
            beta.append(prod)

    if not alpha:
        return {non_terminal: productions}

    new_nt = non_terminal + "'"
    grammar = {}

    grammar[non_terminal] = [b + new_nt for b in beta]
    grammar[new_nt] = [a + new_nt for a in alpha] + ["ε"]

    return grammar


# --------------------------------
# Left Factoring
# --------------------------------
def left_factoring(non_terminal, productions):
    prefix_map = {}
    for prod in productions:
        prefix = prod[0]
        prefix_map.setdefault(prefix, []).append(prod)

    grammar = {}
    new_prods = []

    for prefix, prods in prefix_map.items():
        if len(prods) > 1:
            new_nt = non_terminal + "'"
            new_prods.append(prefix + new_nt)
            grammar[new_nt] = [p[1:] if len(p) > 1 else "ε" for p in prods]
        else:
            new_prods.append(prods[0])

    grammar[non_terminal] = new_prods
    return grammar


# --------------------------------
# MAIN DRIVER
# --------------------------------
if __name__ == "__main__":

    # 1. Ambiguity
    eliminate_ambiguity()

    # 2. Left Recursion
    print("\n--- Left Recursion Elimination ---")
    grammar_lr = {
        "A": ["Aa", "b"]
    }

    lr_result = eliminate_left_recursion("A", grammar_lr["A"])
    for nt, prods in lr_result.items():
        print(f"{nt} -> {' | '.join(prods)}")

    # 3. Left Factoring
    print("\n--- Left Factoring ---")
    grammar_lf = {
        "B": ["ab", "ac"]
    }

    lf_result = left_factoring("B", grammar_lf["B"])
    for nt, prods in lf_result.items():
        print(f"{nt} -> {' | '.join(prods)}")
