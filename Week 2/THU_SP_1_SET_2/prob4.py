from collections import Counter
def prioritize_observations(observed_species, priority_species):

    counts = Counter(observed_species)

    diff_set = set(observed_species) - set(priority_species)

    diff_list = list(diff_set)
    diff_list.sort()
    new_list=[]
    for i,v in enumerate(priority_species):
        for j in range(counts.get(v),0):
            new_list.append(v)
    print(new_list)
    new_list.extend(diff_list)
    return new_list
  

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 
