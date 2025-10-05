from collections import Counter
def max_species_copies(raised_species, target_species):
  raised_count = Counter(raised_species)
  min_count = min(raised_count.values())
  # return min_count

  min_count = 10000
  for i in target_species:
    if raised_count.get(i,0) < min_count:
      min_count = raised_count.get(i,0)
  return min_count



# raised_species1 = "abcba"
# target_species1 = "abc"
# print(max_species_copies(raised_species1, target_species1))  # Output: 1

# raised_species2 = "aaaaabbbbcc"
# target_species2 = "abc"
# print(max_species_copies(raised_species2, target_species2)) # Output: 2

print(max_species_copies("abcba", "abc"))        # 1
print(max_species_copies("aaaaabbbbcc", "abc"))  # 2
print(max_species_copies("aabbaa", "aab"))       # 2
print(max_species_copies("aabc", "aab"))  
print(max_species_copies("abc", "abcd"))