from pathlib import Path
from nuels_fun_with_peptides.file_handling import read_fasta

TEST_DATA = Path(__file__).parent/ "test_data"

def test_fasta_reader():
    tmp_fasta_path = TEST_DATA / "dummy_proteins.fasta"
    protein_map = read_fasta(tmp_fasta_path)
    
    # Replace the strings with your fasta content
    # which you expect to be now available as a dictionary
    assert protein_map["PROTEIN_ID_1"] == "DUMMYSEQUENCEONE"
    assert protein_map["PROTEIN_ID_2"] == "DUMMYSEQUENCETWO"