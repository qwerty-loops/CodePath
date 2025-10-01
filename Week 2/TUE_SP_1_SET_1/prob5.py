def best_set(votes):
    count_vote={}
    for i,v in votes.items():
        if v not in count_vote:
            count_vote[v]=1
        else:
            count_vote[v]+=1
    max_vote = max(count_vote.values())

    for i,v in count_vote.items():
        if v==max_vote:
            return i

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
