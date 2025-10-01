def find_stage_arrangement_difference(s, t):
    d=0
    for i, v1 in enumerate(s):
        for j, v2 in enumerate(t):
            if v1==v2:
                d+=abs(i- j)
    return d

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))