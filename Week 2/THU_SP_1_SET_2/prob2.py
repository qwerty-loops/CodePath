from collections import Counter

def count_endangered_species(endangered_species, observed_species):
    #
    c=0
    for i in observed_species:
        if i in endangered_species:
            c+=1
    return c


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  