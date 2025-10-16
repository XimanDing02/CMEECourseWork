# dictionary.py
# Only code in this document, all understanding of the code are in readme file.
GenomeSize = {'Homo sapiens': 3200.0, 'Escherichia coli': 4.6, 'Arabidopsis thaliana': 157.0}
print(GenomeSize)

print(GenomeSize['Arabidopsis thaliana'])

GenomeSize['Saccharomyces cerevisiae'] = 12.1
print(GenomeSize)

GenomeSize['Escherichia coli'] = 4.6 
print(GenomeSize)

GenomeSize['Homo sapiens'] = 3201.1
print(GenomeSize)

# Define a dictionary with duplicate keys
my_dict = {'a': 1, 'b': 2, 'a': 3}

# Print the dictionary
print(my_dict)