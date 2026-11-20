from nuels_fun_with_peptides.mass_spectra_simulation import calculate_mol_mass, calculate_mol_mass_collection, calculate_mz_collection, fragment_peptide

def test_calculate_mol_mass():
    aa_mass_dict = {'N':10,
                    'i': 5, 
                    'l': 2.5,
                    's': 2.5
                    }
    test_peptide = "Nils"
    test_wrong_peptide = "Nols"
    expected_mass = 20.0
    calculated_mass = calculate_mol_mass(test_peptide, aa_mass_dict)[1][test_peptide]
    wrong_calculation = calculate_mol_mass(test_wrong_peptide, aa_mass_dict)
    assert calculated_mass == expected_mass
    assert wrong_calculation == (False, "404 Either you or the mass table didn't now this one: o")

test_calculate_mol_mass()


def test_calculate_mol_mass_collection():
    aa_mass_dict = {
        "P": 10.0,
        "E": 5.0,
        "T": 20.0
    }
    peptides = ["PETE", "PEE"]
    expected = {
        "PETE": 40.0,
        "PEE": 20
    }
    actual = calculate_mol_mass_collection(peptides,aa_mass_dict)

    assert actual == expected

test_calculate_mol_mass_collection()

def test_calculate_mz_collection():
    peptide_mass_map = {"PEPTIDE":799.3599}
    actual = calculate_mz_collection(peptide_mass_map, charge=2)
    expected = {"PEPTIDE": 400.68695}

    assert actual == expected

test_calculate_mz_collection()


def test_fragment_peptide():
    peptide = "PEPT"
    expected = ['P', 'PE', 'PEP', 'T', 'TP', 'TPE']
    actual = fragment_peptide("PEPT")

    assert actual == expected
    assert "PEPT" not in expected  # which string should not be in the expected?

test_fragment_peptide()