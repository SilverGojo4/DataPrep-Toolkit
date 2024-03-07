# Data Preprocessing

This repository contains a collection of Python scripts for data preprocessing tasks. These scripts provide various functionalities, including converting data files to standard formats, cleaning and processing data, comparing datasets, etc.

## Project Structure

The toolkit is organized as follows:

- `tsv_to_csv.py`: This script converts .tsv format files to .csv format
- `transpose_df_to_csv.py`: This script transposes a DataFrame and saves it as a CSV file
- `shuffle_split_to_csv.py`: This script shuffles a dataset and splits it into training and testing sets, then saves them to specified paths
- `seq_length.py`: This script calculates the length of each sequence and adds it to the DataFrame
- `seq_length_cut.py`: This script filters sequences based on their length, keeping only those within a specified range
- `py_ipynb.py`: This script provides functionality to convert Python source code files (.py) to Jupyter Notebook files (.ipynb) and vice versa
- `nature_amino_acid.py`: This script filters sequences to include only natural amino acids
- `fasta_to_dataframe.py`: This script converts FASTA files to a DataFrame
- `compare_df.py`: This script compares two DataFrames and identifies differences
- `calculate_atomic_mass.py`: This script calculates the atomic mass for each sequence in a DataFrame and adds it as a new column