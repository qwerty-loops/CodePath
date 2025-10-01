def identify_conflicts(venue1_schedule, venue2_schedule):
    conf_schedule={}
    for i,j in zip(venue1_schedule,venue2_schedule):
        if i==j and venue1_schedule[i]==venue2_schedule[j]:
            conf_schedule[i]=venue1_schedule[i]
    return conf_schedule

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))