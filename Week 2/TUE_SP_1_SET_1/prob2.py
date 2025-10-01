def get_artist_info(artist, festival_schedule):
    # for i,v in festival_schedule.items():
    #     if i == artist:
    #         return v
    #     else:
    #         return "{'message': 'Artist not found'}"

    for i,v in enumerate(festival_schedule):
        if v == artist:
            return festival_schedule[v]

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  