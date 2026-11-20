from nuels_fun_with_peptides.protein_digestion import digest_protein_sequence, digest_protein_collection, compute_sequence_coverage
from nuels_fun_with_peptides.variables import enzyme_cleavage_patterns

def test_digest_protein_sequence():
    dummy_seq_1 = "DADADAKDAAKDADADADADADADADADADADADADADADADAK"    #test if the length filter works
    dummy_seq_2 = "RISRISRISKZRISRISRISRISKPRISRISRISA"             #tests another sequence    
    dummy_pattern1 = enzyme_cleavage_patterns['LysC']
    dummy_pattern2 = enzyme_cleavage_patterns['Trypsin']
    dummy_pattern3 = '(?<=Z)'                                       #test if another pattern can be implemented      
    

    assert digest_protein_sequence(dummy_seq_1, dummy_pattern1) == ["DADADAK"]
    assert digest_protein_sequence(dummy_seq_2, dummy_pattern1) == ['RISRISRISK', 'ZRISRISRISRISK', 'PRISRISRISA']
    assert digest_protein_sequence(dummy_seq_2, dummy_pattern2) == ['ISKPR']
    assert digest_protein_sequence(dummy_seq_2, dummy_pattern3) == ['RISRISRISKZ', 'RISRISRISRISKPRISRISRISA']

test_digest_protein_sequence()

def test_digest_protein_collection():
    dummy_proteins = {
        "Dummy1":"TESTTESTTESTKTEST",
        "Dummy2":"DIDODIDODIDODIDODIOK"
    }

    assert digest_protein_collection(dummy_proteins, enzyme_cleavage_patterns["LysC"], 5, 30) == {"Dummy1":["TESTTESTTESTK"], "Dummy2":["DIDODIDODIDODIDODIOK"] }

test_digest_protein_collection()

def test_compute_sequence_coverage():
    dummy_prot_seq = "TESTTESTTESTTESTBBAUMBAUMBAUMPET"
    dummy_peps = ['TESTTESTTESTTEST', "KRASSER"]

    coverage = compute_sequence_coverage(dummy_prot_seq, dummy_peps)
    assert coverage == 50.00

test_compute_sequence_coverage()