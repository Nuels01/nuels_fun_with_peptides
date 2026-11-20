# nuels_fun_with_peptides


## Description
This is a short project for our practical course "advanced python course". It takes a .fasta file with a list of proteins. The program will simulate the digestion of the proteins, a liquid chromatography and finaly a mass spectrometer. 

!!! the code is still under development !!!

## Requirements


### Packages

- numpy

- pandas

- matplotlib

- pyteomics

- ipykernel

- pytest

### Instalation

```
git clone https://github.com/Nuels01/nuels_fun_with_peptides
cd nuels_fun_with_peptides
pip install -e .
```



## How to use the package

The package simulates a simple bottom-up proteomics workflow in four steps:

**FASTA file → protein digestion → liquid chromatography → mass spectrometry**

A complete walkthrough is available in [`tutorials/ms_experiment_final.ipynb`](tutorials/ms_experiment_final.ipynb).

```python
import nuels_fun_with_peptides as nfp
```

### 1. Read a FASTA file

```python
protein_map = nfp.read_fasta("data/sample_proteins.fasta")
# {'P11802': 'MATSRYEPVAEIGVGAYGTVYK...', ...}
```

Returns a dictionary `{protein_id: sequence}`.

### 2. Digest proteins into peptides

Available enzymes are stored in `nfp.enzyme_cleavage_patterns`: `LysC`, `LysN`, `ArgC`, `Trypsin`.

```python
trypsin = nfp.enzyme_cleavage_patterns["Trypsin"]

# a single protein
peptides = nfp.digest_protein_sequence(protein_map["P11802"], trypsin)

# all proteins at once -> {protein_id: [peptides]}
peptide_map = nfp.digest_protein_collection(protein_map, trypsin, min_pep_len=5, max_pep_len=30)

# share of the protein sequence covered by the peptides (in %)
coverage = nfp.compute_sequence_coverage(protein_map["P11802"], peptides)
```

Only peptides with a length between `min_pep_len` and `max_pep_len` (default 5–30) are kept.

### 3. Simulate the liquid chromatography

Retention times are predicted with the additive model `pyteomics.achrom` (`RCs_guo_ph7_0`).

```python
pooled_peptides = sum(peptide_map.values(), [])

retention_times = nfp.predict_lc_retention_times(pooled_peptides)
# {'WVTFISLLLLFSSAYSR': 83.5, 'SEIAHR': 11.8, ...}

nfp.plot_retention_time(retention_times, resolution=30)   # histogram

selected = nfp.select_retention_time_window(retention_times, lower_ret_time=0, upper_ret_time=20)
# ['SEIAHR', ...]
```

### 4. Simulate the mass spectrometer

```python
# molecular mass = sum of the amino acid masses (nfp.amino_acid_mass_dalton)
mass_map = nfp.calculate_mol_mass_collection(selected, nfp.amino_acid_mass_dalton)
# {'SEIAHR': 693.77, ...}

# m/z values for a given charge state
mz_map = nfp.calculate_mz_collection(mass_map, charge=2)
# {'SEIAHR': 347.892, ...}

# MS1 spectrum with random intensities (reproducible via seed)
nfp.plot_spectrum(mz_map, random_count_range=(0, 30000), seed=42)

# b- and y-ion series of a single peptide
nfp.fragment_peptide("PEPT")
# ['P', 'PE', 'PEP', 'T', 'TP', 'TPE']
```

## Function overview

| Module | Function | Description |
|---|---|---|
| `file_handling` | `read_fasta` | Reads a FASTA file into `{id: sequence}` |
| `protein_digestion` | `digest_protein_sequence` | Digests one sequence with a regex cleavage pattern |
| | `digest_protein_collection` | Digests all proteins of a protein map |
| | `compute_sequence_coverage` | Sequence coverage of a protein in % |
| `liquid_chormatography` | `predict_lc_retention_times` | Predicts retention times with `pyteomics.achrom` |
| | `plot_retention_time` | Histogram of the retention times |
| | `select_retention_time_window` | Peptides within a retention time window |
| `mass_spectra_simulation` | `calculate_mol_mass` / `calculate_mol_mass_collection` | Molecular mass of one / many peptides |
| | `calculate_mz_collection` | m/z values for a charge state |
| | `plot_spectrum` | MS1 spectrum with random intensities |
| | `fragment_peptide` | b- and y-ion series |
| `variables` | `enzyme_cleavage_patterns`, `amino_acid_mass_dalton` | Cleavage patterns and amino acid masses |

## Running the tests

```bash
pytest
```

Tests are located in `tests/` and run automatically on every push via GitHub Actions.

## Notes and limitations

- Sequences with non-standard amino acids (e.g. `X`, `B`, `Z`, `U`) can not be handled by the retention time prediction.
- Molecular masses are the sum of the residue masses; the mass of water is not added.
- The spectrum intensities are random and only meant for visualization.

## License

This project is licensed under the MIT License – see [LICENSE](LICENSE).

