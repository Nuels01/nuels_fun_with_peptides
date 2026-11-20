

def calculate_mol_mass(peptide_seq, amino_acid_mass_dict):
    """
    calculates the mass of a single given peptide sequence.

    Parameters
    ----------
    peptide_seq: str
            contains the peptide sequence
    
    amino_acid_mass_dict: dict
            contains the molecular mass of different Amino acids 
    Returns
    -------
    dict: 
            contains the peptidesequence and its mass
    """
    molecular_weigth = 0.0
    molecular_weigth_dict = {}
    for amino_acid in peptide_seq: 
        if amino_acid in amino_acid_mass_dict.keys(): 
            molecular_weigth = molecular_weigth + amino_acid_mass_dict[amino_acid]
        else: 
            return False, ("404 Either you or the mass table didn't now this one: " + amino_acid)

    molecular_weigth_dict[peptide_seq] = molecular_weigth

    return True, molecular_weigth_dict


def calculate_mol_mass_collection(peptides, amino_acid_mass_dict):
    """
    Calculates the molecular masses of multiple peptides.
    
    Parameters
    ----------
    peptides: list of strings
            contains the sequences of the peptides 
    
    amino_acid_mass_dict
            contains the weigth of the amino acids
    Returns
    -------
    dict: 
            contains the peptides and their molecular masses 
    """
    mol_mass_collection = {}

    if type(peptides) == list:
        for seq in peptides:
            if type(seq) == str: 
                part_solution = calculate_mol_mass(seq, amino_acid_mass_dict)
                if part_solution[0]:
                    mol_mass_collection.update(part_solution[1])
                else: 
                    mol_mass_collection.update({seq:part_solution[1]})
            else: 
                return ("There was a " + str(type(seq)) + " and string was expected!")
    else: 
        return (str(type(peptides)) + " is not even a list you seggl")

    return mol_mass_collection


def calculate_mz_collection(peptide_mass_map, charge=2, proton_mass=1.007):
    """
    Calculates the m/z values for given peptides.

    Parameters
    ----------
    peptide_mass_map: dict
            contains the peptides and their mass
    
    charge: float
            contains the charge value 

    Returns
    -------
    dict: 
            contains the peptides and their m/z values

    """
    m_z_values = {}
    if type(peptide_mass_map) == dict: 
        for pep, mass in peptide_mass_map.items(): 
            if type(mass) == str: 
                continue
            else: 
                current_m_z = (mass + charge * proton_mass) / charge
                m_z_values[pep] = current_m_z
        return m_z_values
    else: 
        return "that was a " + str(type(peptide_mass_map)) + " and not a dictionary dumbatz"


import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(mz_values,  random_count_range=(0, 30000), seed=42):
    """
    Plots a bar chart of m/z values with an option to implement random count_ranges to simulate detector noise.

    Parameters
    ----------
    mz_values: dict, list
            contains peptides and/or their m/z values
    
    random_count_range: float 
            enables random values for simulating noises
    
    seed: int
            the seed for the random number generator to make it reproducable

    Returns
    -------
    none
    """
    present_values_mz = []
    if type(mz_values) == dict: 
        present_values_mz = mz_values.values()
    elif type(mz_values) != list: 
        return "not a list or a dict"

    low, high = random_count_range
    np.random.seed(seed)
    randomize = np.random.randint(low, high, len(mz_values))
    
    
    
    plt.bar(present_values_mz, randomize, width=10)
    plt.plot()


def fragment_peptide(peptide):
    """
    makes a b-ion and a y-ion series of a given peptide.

    Parameters
    ----------
    peptide: str
            contains the sequence of the peptide
    Returns
    -------
    list: 
            contains the b-ion and y-ion series of the peptide
    """
    try:
        peptide_reverse = peptide[::-1]
        #print(peptide_reverse)
        bion_series = []
        yion_series = []
        count = 1
        for char in peptide: 
            if count != len(peptide):
                bion_series.append(peptide[:count])
                yion_series.append(peptide_reverse[:count])
                count += 1
            else: 
                break
        bion_series.extend(yion_series)

        return bion_series
        
    except TypeError: 
        return str(type(peptide)) + " is not a string!"