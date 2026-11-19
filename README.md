# nuels_fun_with_peptides


## Description
This is a short project for our practical course "advanced python course". It takes a .fasa file with a list of proteins. The program will simulate the digestion of the proteins, a liquid chromatography and finaly a mass spectrometer. 

!!! the code is still under development !!!

## Requirements


The following packages will be needed: 

- numpy

- pandas

- matplotlib

- pyteomics

- ipykernel

- pytest

You can use 
```pip install -r requirements.txt```
to install all of them automatically.

## How to use the Package

You need a .fasa file with a list of proteins in your folder. 

```read_fasta(FILEPATH) ```  

You digest the proteins with a choosen pattern.

```digest_protein_collection(PROTEINS, PATTERN)```

