def distinct_averages(species_populations):
#   new_averages=[]
#   sp_copy= species_populations[:]
#   while sp_copy:
#     min_species = min(sp_copy)
#     max_species = max(sp_copy)
#     avg = (min_species + max_species)/2
#     new_averages.append(avg)
#     sp_copy.remove(min_species)
#     sp_copy.remove(max_species)

    
#   if len(new_averages)==1:
#     return 1
#   else:
#     return len(set(new_averages))

#OR - Two pointer

    species_populations.sort()
    low,high=0,len(species_populations)-1
    new_averages=[]
    while low<high:
        avg = (species_populations[low] + species_populations[high])/2
        new_averages.append(avg)
        low+=1
        high-=1

    if len(new_averages)==1:
        return 1
    else:
        return len(set(new_averages))



species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 