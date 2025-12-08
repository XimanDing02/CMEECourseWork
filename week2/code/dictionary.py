#!/usr/bin/env python3

"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: dictionary.py
Des: Create a dictionary that maps taxonomic orders to sets of species
     using both conventional loops and list comprehensions.
Usage: python3 dictionary.py (in terminal)
Date: Nov, 2025
"""

# Docstrings are considered part of the running code (normal comments are
# stripped). Hence, you can access your docstrings at run time.

__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

# Constants
taxa = [
    ('Myotis lucifugus', 'Chiroptera'),
    ('Gerbillus henleyi', 'Rodentia'),
    ('Peromyscus crinitus', 'Rodentia'),
    ('Mus domesticus', 'Rodentia'),
    ('Cleithrionomys rutilus', 'Rodentia'),
    ('Microgale dobsoni', 'Afrosoricida'),
    ('Microgale talazaci', 'Afrosoricida'),
    ('Lyacon pictus', 'Carnivora'),
    ('Arctocephalus gazella', 'Carnivora'),
    ('Canis lupus', 'Carnivora'),
]

# Functions
def build_taxa_dict_loop(taxa_list):
    """Create a dictionary mapping order names to sets of species using a loop."""
    taxa_dic = {}
    # Loop through each (species, order) pair
    for species, order in taxa_list:
        if order not in taxa_dic:
            taxa_dic[order] = set()
            # Add the species to the corresponding set
        taxa_dic[order].add(species)
    return taxa_dic


def build_taxa_dict_comprehension(taxa_list):
    """Create the same dictionary using dictionary and set comprehensions."""
    return {order: {species for species, o in taxa_list if o == order}
            for order in {o for _, o in taxa_list}}


def print_taxa_dict(taxa_dic):
    """Print the taxa dictionary in a formatted way."""
    for order, species_set in taxa_dic.items():
        print(f"'{order}': {species_set}")


## Main ##
def main(argv):
    """Main entry point of the program."""
    print("Dictionary created using a loop:\n")
    taxa_dic_loop = build_taxa_dict_loop(taxa)
    print_taxa_dict(taxa_dic_loop)

    print("\nDictionary created using comprehensions:\n")
    taxa_dic_comp = build_taxa_dict_comprehension(taxa)
    print_taxa_dict(taxa_dic_comp)

    return 0


if __name__ == "__main__":
    import sys
    status = main(sys.argv)
    sys.exit(status)