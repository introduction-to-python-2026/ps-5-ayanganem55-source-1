
from string_utils import count_atoms_in_molecule as count_atoms_in_reaction


from equation_utils import build_equations, my_solve


def parse_chemical_reaction(reaction_string):
    """Parses a string like 'A + B -> C + D' into a tuple of (reactants_list, products_list)."""
    if "->" not in reaction_string:
        raise ValueError("Reaction string must contain '->'")
    
    parts = reaction_string.split("->")
    reactants_str = parts[0].strip()
    products_str = parts[1].strip()

    reactants_list = [c.strip() for c in reactants_str.split("+")]
    products_list = [c.strip() for c in products_str.split("+")]

    return reactants_list, products_list


def balance_reaction(reaction): 

    
    
    reactants, products = parse_chemical_reaction(reaction) 
    
    
    reactant_atoms = [count_atoms_in_reaction(r) for r in reactants] 
    product_atoms = [count_atoms_in_reaction(p) for p in products]

   
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    coefficients = my_solve(equations, coefficients) + [1]

    return coefficients 


if __name__ == '__main__':
    
    reaction_str = "Fe2O3 + H2 -> Fe + H2O"
    print(f"Balancing reaction: {reaction_str}")
    
    


