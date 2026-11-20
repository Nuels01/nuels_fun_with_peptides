import re

def digest_protein_sequence(protein_seq, cleave_pattern, min_pep_len=5, max_pep_len=30):
    """
    Cleavege of protein sequences with a specific pattern and filters after a set lenght

    Parameters
    ----------
    protein_seq: str
            the protein sequence
    
    cleave_pattern: str
            the pattern that is used for cleavage 
    
    min_pep_len: int
            the minimal length a sequence can have after cleavage without being filtered out 
    
    max_pep_len: int 
            the maximal length a sequence can have after cleavage without being filtered out
    
    Returns
    -------
    list 
            contains all cleaved and filtered sequences
    """
    peptides = re.split(cleave_pattern, protein_seq)
    filtered_peptides = [p for p in peptides if len(p) >= min_pep_len and len(p) <= max_pep_len]
    return filtered_peptides


def digest_protein_collection(protein_map, cleave_pattern, min_pep_len=5, max_pep_len=30):
    """
    Takes a collection of proteins, digests them and returns the peptides

    Parameters
    ----------
    protein_map: dic
            has the proteins and their sequencences
    
    cleavage_pattern: str
            the pattern that is used for digestion 
    
    min_pep_len: int
            the minimal length a peptide must have to be noted 
    
    max_pep_len: int 
            the maximal length a peptide can have to be noted
    Returns
    -------
    dic:
            the list of peptides that are filtered by length
    """

    digested_protein_map = {}
    for id, protein_sequence in protein_map.items(): 
          digested_protein_map[id] = digest_protein_sequence(protein_sequence, cleave_pattern, min_pep_len, max_pep_len)

    return digested_protein_map


def compute_sequence_coverage(protein_seq, peptides):
    """
    Calculates how much of a protein seqnece is covered by a enzyme

    Parameters
    -------
    protein_seq: str 
            the whole sequence
    
    peptides: array
            the peptides that are testet
    Returns
    -------
    float: 
            how many percantage are covered 
    """
    coverage = 0.0
    sequence_length = len(protein_seq)
    for p in peptides: 
        if p in protein_seq: 
                coverage = coverage + ((len(p) / sequence_length) *100)
        else: 
             continue
    return coverage