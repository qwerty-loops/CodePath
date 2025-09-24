def lineup(artists, set_times):
    

    result={}
    for artist,set_time in zip(artists,set_times):
        result[artist] = set_time
    return result




artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]



artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))