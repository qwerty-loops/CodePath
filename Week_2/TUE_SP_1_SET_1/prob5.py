def best_set(votes):
    
    hivote={}
    for vote in votes.values():
        if vote not in hivote:
            hivote[vote]=1
        else:
            hivote[vote]+=1

    for artist,votes in hivote.items():
        if max(hivote.values()) == votes:
            return artist


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