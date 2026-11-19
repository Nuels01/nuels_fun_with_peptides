def read_fasta(filepath :str) -> dict: #str and dict for a ligther design
    """
    Reads a given FASTA file and returns the number of proteins and their sequence sizes.

    Parameters
    ------------
    filepath: str 
                the path to the file that should be read

    Returns
    ------------
    proteinmap: dic 
                contains each protein with id and sequence
    """

    protein_map = {}                                                    #creates an empty dictionary
    current_id = None                                                   #creates an variable with the value None
    current_sequence = []                                               #creates an empty array

    with open(filepath, 'r') as fasta_handle:                           #reads the file as fasta_handle
        for line in fasta_handle:                                       #goes trough every lie
            stripped = line.strip()                                     #gets rid of white spaces -> it transforms the string ino a more clean form
            if not stripped:                                            #tests if the line is empty and if so jumps to the next line
                continue
            if stripped.startswith('>'):                                #is activated when the line starts with > 
                if current_id is not None:                              #checks the current id
                    protein_map[current_id] = ''.join(current_sequence)
                    current_sequence = []
                current_id = stripped.split('|')[1]
            else:
                current_sequence.append(stripped)                       #attaches the stripped lines into the current_sequence id 

    if current_id is not None:
        protein_map[current_id] = ''.join(current_sequence)             #saves the last line because it wouldn't get into it due to the end of the file

    return protein_map

