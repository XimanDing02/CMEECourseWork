#!/usr/bin/env python3
"""
Description:
    This program creates a dictionary mapping mammalian order names to sets of species.
    It demonstrates two approaches:
        1. Using a conventional for loop
        2. Using dictionary and set comprehensions
"""

__appname__ = 'taxa_dictionary'
__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '1.0.0'
__license__ = 'MIT'

## Imports ##
# (No external libraries needed for this task)

## Constants ##
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

## Functions ##
def build_taxa_dict_loop(taxa_list):
    """Create a dictionary mapping order names to sets of species using a loop."""
    taxa_dic = {}
    for species, order in taxa_list:
        if order not in taxa_dic:
            taxa_dic[order] = set()
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