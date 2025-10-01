def num_popular_pairs(popularity_scores):
    ps={}
    for i in popularity_scores:
        if i not in ps:
            ps[i]=1
        else:
            ps[i]+=1
    # return ps

    s=0
    for i,v in ps.items():
        if v>1:
            s+=(v*(v-1))//2
    return s

            


popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]
popularity_scores4 = [5, 7, 5, 5, 7]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))
print(num_popular_pairs(popularity_scores4)) 