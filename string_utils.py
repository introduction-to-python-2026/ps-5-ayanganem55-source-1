


import re

def split_before_uppercases(formula):
    """
    Splits a chemical formula string into individual element groups 
    by inserting a space before every uppercase letter that is not at the start.
    Example: 'NaClH2O' -> 'Na Cl H2O'
    """
    
    return re.sub(r'(?<!^)([A-Z])', r' \1', formula).strip()


def split_at_digit(element_group):
    """
    Splits an element group string into a tuple of (element name, count string).
    Example: 'H2' -> ('H', '2'), 'O' -> ('O', '')
    """
    
    match = re.findall(r'([A-Za-z]+)(\d*)', element_group)
    if match:
        # Returns the first tuple found: (element_symbol, count_string)
        return match[0]
    return ('', '')


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    # Note: I am using my completed functions 'split_before_uppercases' and 'split_at_digit'
    # as replacements for the placeholder names 'split_by_capitals' and 'split_at_number' 
    # mentioned in your prompt's template.
    for atom_group_str in split_before_uppercases(molecular_formula).split():
        atom_name, count_str = split_at_digit(atom_group_str)
        
        # Step 2: Update the dictionary with the atom name and count
        # Convert count string to integer (defaults to 1 if string is empty)
        count = int(count_str) if count_str else 1
        
        if atom_name in atom_counts:
            atom_counts[atom_name] += count
        else:
            atom_counts[atom_name] = count

    # Step 3: Return the completed dictionary
    return atom_counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
